from django.shortcuts import render, redirect
from django.db.models import QuerySet
from .models import Report, Invoice, InvoiceItem
import json
from django.db.models import Count, Sum
from .forms import CreateReportForm
from django.db.models.functions import TruncMonth


def reports(request):
    reports = Report.objects.all()
    return render(request, 'reports.html', {'reports': reports})


def create_report(request):
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


def show_text_report(request, id):
    report = Report.objects.get(id=id)

    range = InvoiceItem.invoice
    print(range)

    query = InvoiceItem.objects.filter(id=id).query
    query.group_by = ['product']

    results = QuerySet(query=query, model=InvoiceItem)

    return render(request, 'text_report.html', {'report': report, 'obj': results, 'range': range})


def show_visual_report(request, id):
    report = Report.objects.get(id=id)

    grouped = report.invoices.all() \
        .annotate(month=TruncMonth('date_of_issue')) \
        .values('month') \
        .annotate(c=Count('id'), s=Sum('invoice_item__quantity')) \
        .values('month', 'c', 's', 'invoice_item__product__name')

    mts = report.invoices.all() \
        .annotate(month=TruncMonth('date_of_issue')) \
        .values('month') \
        .annotate(c=Count('id'), s=Sum('invoice_item__quantity')) \
        .values('month').distinct()

    months = list()
    obj = dict()
    products = list()
    all_products = report.invoices.all().values('invoice_item__product__name').distinct()

    # Add months
    for month in grouped:
        mth = month['month'].strftime('%Y-%m')
        months.append(mth)
        obj.update({mth: {}})

    results = grouped



    for product in all_products:
        products.append(product['invoice_item__product__name'])

    print('Products count:' + str(len(products)))
    months_number = len(months)
    print('montsh ' + str(len(mts)))
    listOfLists = []

    for x in range(len(mts)):
        listOfLists.append(x)
        listOfLists[x] = [0] * len(all_products)

    for x in range(months_number):
        for index, elem in enumerate(grouped):
            for key, val in obj.items():
                if key == elem['month'].strftime('%Y-%m'):
                    obj[key].update({elem['invoice_item__product__name']: elem['s']})

    print(listOfLists)

    #działa
    # for index, product in enumerate(grouped):
    #     for key, val in obj.items():
    #         for k, v in val.items():
    #             for i, p in enumerate(products):
    #                 if product['invoice_item__product__name'] == k and product['month'].strftime('%Y-%m') == key and product['invoice_item__product__name'] == p:
    #                     quantity[i] = v
    #                 elif product['invoice_item__product__name'] == k and not product['month'].strftime('%Y-%m') == key and product['invoice_item__product__name'] == p:
    #                     quantity2[i] = v


    for ind, val in enumerate(listOfLists):
        for index, product in enumerate(grouped):
            for key, val in obj.items():
                for k, v in val.items():
                    for i, p in enumerate(products):
                        if product['invoice_item__product__name'] == k and product['month'].strftime('%Y-%m') == key and product['invoice_item__product__name'] == p:
                            listOfLists[0][i] = v
                        elif product['invoice_item__product__name'] == k and not product['month'].strftime('%Y-%m') == key and product['invoice_item__product__name'] == p:
                            listOfLists[1][i] = v

    #TODO: dodawanie dynamicznie list

    # print('Dictionary')
    # print(obj)
    # print('quantity1')
    # print(quantity)
    # print('quantity2')
    # print(quantity2)

    series = []
    print(listOfLists)
    for index, elem in enumerate(listOfLists):
        print('series')
        series.append({
            'name': mts[index]['month'].strftime('%Y-%m'),
            'data': elem,
            'color': 'green'
        })


    survived_series = {
        'name': months[0],
        'data': listOfLists[0],
        'color': 'green'
    }

    not_survived_series = {
        'name': months[1],
        'data': listOfLists[1],
        'color': 'red'
    }

    chart = {
        'chart': {'type': 'column'},
        'title': {'text': 'Titanic Survivors by Ticket Class'},
        'xAxis': {'categories': products},
        # 'series': [survived_series, not_survived_series]
        'series': series
    }

    chart = json.dumps(chart)

    return render(request, 'visual_report.html', {
        'chart': chart,
        'obj': results,
        'report': report,
        'products': products
    })




