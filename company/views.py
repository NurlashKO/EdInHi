from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def company(requests, company_id):
    return HttpResponse("Company : " + str(company_id))
