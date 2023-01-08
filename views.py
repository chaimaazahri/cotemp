import csv

from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
# Create your views here.
from .models import Dht
from django.views.generic.base import TemplateView


def home(request):
    return render(request, 'home.html')


def dht11(request):
    tab = Dht.objects.all()
    s = {'tab': tab[len(tab)-72:len(tab)]}
    return render(request, 'temperature.html', s)


def dht12(request):
    tab = Dht.objects.all()
    s = {'tab': tab[len(tab)-72:len(tab)]}
    return render(request, 'graphe.html', s)


def exp_csv(request):
    obj = Dht.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=DHT.csv'
    writer = csv.writer(response)
    writer.writerow(['ID',  'Temp',  'DT'])

    studs = obj.values_list('id',  'temp',  'dt')[len(obj)-36:len(obj)]
    for std in studs:
        writer.writerow(std)
    return response

# Create your views here.
