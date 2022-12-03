from django.http import HttpResponse
from django.template.loader import get_template
from django.views import generic
from django.shortcuts import render, get_object_or_404


import datetime


# class saludo(generic.TemplateView):

#     template_name= 'base.html'

def saludo(request):

    # plantilla = get_template('base.html')
    return render(request, 'base.html')

def age(request, year):

    edad_actual = 43
    periodo= year - 2022

    edad_futura= edad_actual + periodo

    documento= "En el año %s tendrás %s años" %(year, edad_futura)

    return HttpResponse(documento)





