from django.shortcuts import render, redirect, HttpResponse
from django.db.models import QuerySet
from .models import Report, Invoice, InvoiceItem
from pprint import pprint
import json
from django.db.models import Count, Q, Sum


def reports(request):
    reports = Report.objects.all()
    return render(request, 'reports.html', {'reports': reports})


def create_report(request):
    return render(request, 'create_report.html')


def show_text_report(request, id):
    report = Report.objects.get(id=id)
    return render(request, 'text_report.html', {'report': report})


def show_visual_report(request, id):
    report = Report.objects.get(id=id)
    dump = pprint(report)
    # invoice = Invoice.objects.get(id=1)
    # report.invoices.add(invoice)

    query = InvoiceItem.objects.all().query
    query.group_by = ['product']
    results = QuerySet(query=query, model=InvoiceItem)
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
    for entry in set:
        categories.append(entry['quantity_count'])
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
    #
    return render(request, 'visual_report.html', {'chart': dump, 'obj': results})
    # return render(request, 'visual_report.html', {'chart': chart})
