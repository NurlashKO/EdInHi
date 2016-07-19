from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import CompanyForm, VacancyForm, TaskForm
from .models import Vacancy


def company_view(request):
    cform = CompanyForm()
    if request.user.is_authenticated():
        if request.user.abstractuser.is_company == False:
            return redirect('/profile')
        if request.method == "POST":
            cform = CompanyForm(request.POST, request.FILES, instance=request.user.abstractuser)
            if cform.is_valid():
                if 'logo' in request.FILES:
                    cform.logo = request.FILES['logo']
                cform.save()
                return redirect('/company')
            return redirect('/company')
        else:
            return render(request, 'company/company.html', {'user': request.user.abstractuser,
                                                            'vacancies': request.user.abstractuser.vacancies.all().count()})
    else:
        return redirect("company_reg")


@login_required
def company_add_vacancy(request):
    vform = VacancyForm(prefix='vform')
    tform = TaskForm(prefix='tform')
    if (request.method == "POST"):
        vform = VacancyForm(request.POST, prefix='vform')
        tform = TaskForm(request.POST, prefix='tform')
        if (vform.is_valid() and tform.is_valid()):
            vacancy = vform.save(commit=False)
            task = tform.save(commit=False)
            task.save()
            vacancy.save()
            vacancy.task.add(task)
            vacancy.save()
            request.user.abstractuser.vacancies.add(vacancy)
            request.user.abstractuser.save()
            return redirect('/company')
    data = {'vform': vform, 'tform': tform}
    return render(request, 'company/company_add_vacancy.html', data)

@login_required
def company_delete_vacancy(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    if request.method == 'POST':
        request.user.abstractuser.vacancies.remove(vacancy)
        vacancy.delete()
        request.user.abstractuser.save()
    return redirect("/company")


@login_required
def company_edit_vacancy(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    form = VacancyForm(request.POST or None, instance=vacancy)
    if form.is_valid():
        form.name = request.POST['name']
        form.description = request.POST['description']
        form.salary = request.POST['salary']
        form.save()
        return redirect('/company')
    return render(request, 'company/company_edit_vacancy.html', {'form': form, 'vacancy': vacancy})


@login_required
def all_vacancies(request):
    all = request.user.abstractuser.vacancies.all()
    return render(request, 'company/vacancies.html', {'vacancies': all})
