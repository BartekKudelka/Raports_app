from django.shortcuts import render, redirect, HttpResponse
from django.db.models import QuerySet
from .models import Report, Invoice, InvoiceItem, Product
from pprint import pprint
import json
from django.db.models import Count, Q, Sum
import datetime


def compare(a, b):
    if a.product == b.product:
        return 1


def reports(request):
    reports = Report.objects.all()
    return render(request, 'reports.html', {'reports': reports})


def create_report(request):
    return render(request, 'create_report.html')


########################################################################################################################

def show_text_report(request, id):
    report = Report.objects.get(id=id)

    q = Invoice.objects.filter(date_of_issue__gte=report.start_date).filter(date_of_issue__lte=report.end_date)

    products = []
    products2 = []

    for invoice in q:
        for item in invoice.invoice_item.all():
            products.append(item)

    products.sort()
    print(products)


    for x in products:
        while len(products)!=0:
            isdouble=False
            it = products.pop()
            for y in products:
                if it.product == y.product:
                    print(y.product)
                    it.quantity = it.quantity + y.quantity
                    it.purchase_value = it.purchase_value+ y.purchase_value
                    products.remove(y)


            products2.append(it)


    print(products2)


    invoices = Invoice.objects.all()
    items = InvoiceItem.objects.all()
    #  for inv in invoices:
    #     if inv.date_of_issue.month >= report.start_date.month and inv.date_of_issue.day >= report.start_date.day\
    #        and inv.date_of_issue.month <= report.end_date.month and inv.date_of_issue.day <= report.end_date.day:

    # print(inv.date_of_issue)
    #       print(i)

    query = InvoiceItem.objects.filter(id=id).query
    query.group_by = ['product']

    results = QuerySet(query=query, model=InvoiceItem)

    return render(request, 'text_report.html', {'report': report, 'obj': results, 'invoices': invoices, 'items': items})


########################################################################################################################

def show_visual_report(request, id):
    report = Report.objects.get(id=id)

    # query = Invoice.objects.values('client').query

    # .annotate(quantity_count=Sum('invoice_item__quantity'))
    # query.group_by = ['invoice_item__product']

    results = QuerySet(query=query, model=Invoice)
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
    #
    return render(request, 'visual_report.html', {'chart': dump, 'obj': results})
    # return render(request, 'visual_report.html', {'chart': chart})
