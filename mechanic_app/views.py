from django.shortcuts import render, redirect
from mechanic_app.models import *
from mechanic_app.forms import  *

# Create your views here.

def index(request):
    return render(request, "index.html")


def repairs(request):
    scheduledRepairs = ScheduledRepair.objects.all()
    if request.method == 'POST':
        scheduled = ScheduledRepairForm(request.POST, request.FILES)
        if scheduled.is_valid():
            scheduled.save()
            redirect("repairs")
    else:
        scheduled = ScheduledRepairForm()


    return render(request, "repairs.html", {"repairs": scheduledRepairs, "form": scheduled})