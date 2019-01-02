from django.shortcuts import render, redirect
from django.db.models import QuerySet
from .models import Report, Invoice, InvoiceItem
import json
from django.db.models import Count, Q, Sum
from .forms import CreateReportForm


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

    # query = Invoice.objects.values('client').query

    # .annotate(quantity_count=Sum('invoice_item__quantity'))
    # query.group_by = ['invoice_item__product']

    # results = QuerySet(query=query, model=Invoice)
    # dataset = Invoice.objects \
    #     .values('start_date') \
    #     .annotate(survived_count=Count('start_date', filter=Q(survived=True)),
    #               not_survived_count=Count('end_date', filter=Q(survived=False))) \
    #     .order_by('start_date')

    set = Invoice.objects \
        .values('invoice_item') \
        .annotate(quantity_count=Sum('invoice_item__quantity', distinct=True))

    dataset = Invoice.objects.values('client', 'date_of_issue', 'invoice_item')
    categories = list()
    products = list()
    quantity = list()
    obj = set
    # for entry in set:
    #     categories.append(entry['quantity_count'])
    # survived_series_data.append(str(entry['date_of_issue']))
    # not_survived_series_data.append(entry['invoice_item'])
    # products.append(str(report.invoices.all()[0].invoice_item.all()[0].product))
    # quantity.append(str(report.invoices.all()[0].invoice_item.all()[0].quantity))

    for invoice in report.invoices.all():
        for invoice_item in invoice.invoice_item.all():
            categories.append(str(invoice_item.product))

            quantity.append((invoice_item.quantity))

    survived_series = {
        'name': 'Survived',
        'data': quantity,
        'color': 'green'
    }

    not_survived_series = {
        'name': 'Survived',
        'data': products,
        'color': 'red'
    }

    chart = {
        'chart': {'type': 'column'},
        'title': {'text': 'Titanic Survivors by Ticket Class'},
        'xAxis': {'categories': categories},
        'series': [survived_series]
    }

    dump = json.dumps(chart)

    return render(request, 'visual_report.html', {'chart': dump, 'obj': obj, 'report': report})
    # return render(request, 'visual_report.html', {'chart': chart})
