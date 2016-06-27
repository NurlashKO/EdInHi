from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from main_app.models import AbstractUser
from company.models import WishList, Vacancy

@login_required
def all_companies(request):
    allCompanies = AbstractUser.objects.filter(is_company=True)
    return render(request, "companies/all_companies.html", {'all_companies' : allCompanies})

@login_required
def detail_company(request, pk):
    company = get_object_or_404(AbstractUser, pk=pk)
    return render(request, 'companies/detail_company.html', {'company' : company})

@login_required
def detail_vacancy(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    return render(request, 'companies/detail_vacancy.html', {'vacancy' : vacancy})

@login_required
def addVacancyUser(request, pk):
    wishlist = WishList.objects.get(pk=request.user.wishlist.id)
    vacancy = Vacancy.objects.get(pk=pk)
    if request.method == 'POST':
        wishlist.vacancy_set.add(vacancy)
    return redirect("all_companies")

