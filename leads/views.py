from django.shortcuts import render
from django.http import HttpResponse
from leads.models import Lead


def lead_list(request):
    leads = Lead.objects.all()
    context = {
        'leads': leads,
    }
    return render(request, "leads/lead_list.html", context)
