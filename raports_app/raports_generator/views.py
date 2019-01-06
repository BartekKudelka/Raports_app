from django.shortcuts import render, redirect
from django.db.models import QuerySet
from .models import Report, Invoice, InvoiceItem, Product, compare
from pprint import pprint
import json
from django.db.models import Count, Sum
from .forms import CreateReportForm
from django.db.models.functions import TruncMonth
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q, Sum






@login_required(login_url='/login/')
def reports(request):
    reports = Report.objects.all().order_by('-start_date')
    return render(request, 'reports.html', {'reports': reports})


@login_required(login_url='/login/')
def create_report(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = CreateReportForm(request.POST)
            if form.is_valid():
                start_date = form.cleaned_data.get('start_date')
                end_date = form.cleaned_data.get('end_date')
                invoices = Invoice.objects.filter(date_of_issue__range=(start_date, end_date))
                report = Report(start_date=start_date, end_date=end_date)
                report.save()
                for invoice in invoices:
                    report.invoices.add(invoice)
                return redirect('reports')
        else:
            form = CreateReportForm()
        return render(request, 'create_report.html', {'form': form})
    return redirect('home')


@login_required(login_url='/login/')
def show_text_report(request, id):
    report = Report.objects.get(id=id)

    q = Invoice.objects.filter(date_of_issue__gte=report.start_date).filter(date_of_issue__lte=report.end_date)

    products = []
    products2 = []

    for invoice in q:
        for item in invoice.invoice_item.all():
            products.append(item)

    for x in range(len(products)):
        products = compare(products)


    prize_sum =0
    quantity_sum =0
    for x in products:
        prize_sum =prize_sum +  x.purchase_value
        quantity_sum = quantity_sum + x.quantity

    return render(request, 'text_report.html', {'report': report, 'items': products, 'qty': quantity_sum, 'val':prize_sum})

@login_required(login_url='/login/')
def show_visual_report(request, id):
    report = Report.objects.get(id=id)

    query_items = report.invoices.all() \
        .annotate(month=TruncMonth('date_of_issue')) \
        .values('month') \
        .annotate(c=Count('id'), s=Sum('invoice_item__quantity')) \
        .values('month', 'c', 's', 'invoice_item__product__name')

    months_query = report.invoices.all() \
        .annotate(month=TruncMonth('date_of_issue')) \
        .values('month') \
        .annotate(c=Count('id'), s=Sum('invoice_item__quantity')) \
        .values('month').distinct()

    all_products = report.invoices.all().values('invoice_item__product__name').distinct()

    items_list = list()
    obj = dict()
    products = list()
    series = []
    list_of_lists = []

    # Add items
    for item in query_items:
        mth = item['month'].strftime('%Y-%m')
        items_list.append(mth)
        obj.update({mth: {}})

    # Add products to list
    for product in all_products:
        products.append(product['invoice_item__product__name'])

    number_of_items = len(items_list)

    # Fill lists with zeros
    for x in range(len(months_query)):
        list_of_lists.append(x)
        list_of_lists[x] = [0] * len(all_products)

    # Fill dictionary with products and sum of products used in given month
    for x in range(number_of_items):
        for index, elem in enumerate(query_items):
            for key, val in obj.items():
                if key == elem['month'].strftime('%Y-%m'):
                    obj[key].update({elem['invoice_item__product__name']: elem['s']})

    # Add sum of products to given month
    for list_index, list_val in enumerate(list_of_lists):
        for index, query_item in enumerate(query_items):
            for dict_date, dict_items in obj.items():
                for dict_product, dict_sum in dict_items.items():
                    for product_index, product in enumerate(products):
                        if query_item['invoice_item__product__name'] == dict_product:
                            if query_item['month'].strftime('%Y-%m') == dict_date:
                                if query_item['invoice_item__product__name'] == product:
                                    if months_query[list_index]['month'].strftime('%Y-%m') == query_item['month'].strftime('%Y-%m'):
                                        list_of_lists[list_index][product_index] = dict_sum


    colors = [
        'green',
        'blue',
        'black',
        'orange',
        'purple',
        'grey',
        '#00f5f5',
        '#00ff22',
        'yellow',
        'red',
        'brown',
        '#ff55ff',
    ]

    for index, elem in enumerate(list_of_lists):
        series.append({
            'name': months_query[index]['month'].strftime('%Y-%m'),
            'data': elem,
            'color': colors[index]
        })

    if len(series) > 0:
        info = 'Data of sales from ' + report.start_date.strftime('%Y-%m-%d') + ' to ' + report.end_date.strftime('%Y-%m-%d')
    else:
        info = 'There was no sales from ' + report.start_date.strftime('%Y-%m-%d') + ' to ' + report.end_date.strftime('%Y-%m-%d')

    chart = {
        'chart': {'type': 'column'},
        'title': {'text': info},
        'xAxis': {'categories': products},
        'series': series
    }

    chart = json.dumps(chart)

    return render(request, 'visual_report.html', {
        'chart': chart,
        'report': report
    })


@login_required(login_url='/login/')
def delete_report(request, id):
    if request.user.is_superuser:
        report = Report.objects.get(id=id)
        report.delete()
    return redirect('reports')


@login_required(login_url='/login/')
def edit_report(request, id):
    if request.user.is_superuser:
        report = Report.objects.get(id=id)
        if request.method == 'POST':
            form = CreateReportForm(request.POST)
            if form.is_valid():
                curr_invoices = report.invoices.all()

                for invoice in curr_invoices:
                    report.invoices.remove(invoice)

                start_date = form.cleaned_data.get('start_date')
                end_date = form.cleaned_data.get('end_date')
                report.start_date = start_date
                report.end_date = end_date
                invoices = Invoice.objects.filter(date_of_issue__range=(start_date, end_date))

                report.save()
                for invoice in invoices:
                    report.invoices.add(invoice)
                return redirect('reports')
        else:
            form = CreateReportForm()
        return render(request, 'edit_report.html', {'form': form, 'report': report})
    return redirect('home')
