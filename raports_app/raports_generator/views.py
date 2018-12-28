from django.shortcuts import render, redirect


def reports(request):
    return render(request, 'reports.html')


def create_report(request):
    return render(request, 'create_report.html')


def show_text_report(request):
    return render(request, 'text_report.html')


def show_visual_report(request):
    return render(request, 'visual_report.html')
