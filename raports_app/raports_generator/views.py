from django.shortcuts import render, redirect, HttpResponse
from .models import Report, Invoice
from pprint import pprint

def reports(request):
    reports = Report.objects.all()
    return render(request, 'reports.html', {'reports': reports})


def create_report(request):
    return render(request, 'create_report.html')


def show_text_report(request):
    return render(request, 'text_report.html')


def show_visual_report(request, id):
    report = Report.objects.get(id=id)
    dump = pprint(report)
    invoice = Invoice.objects.get(id=1)
    report.reports.add(invoice)
    # return render(request, 'visual_report.html', {'report': report, 'dump': dump})
    return HttpResponse({str(vars(report))})