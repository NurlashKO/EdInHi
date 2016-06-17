from django.contrib.auth.decorators import login_required
from django.forms import ModelForm, modelformset_factory
from django.shortcuts import render, get_object_or_404, redirect

from company.models import Vacancy, CompanyTask
from .forms import VacancyForm, TaskForm

def company_view(request):
    if request.user.is_authenticated():
        if request.method == "POST":
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                new_name = request.POST['name']
                new_webpage = request.POST['webpage']
                new_contact_phone = request.POST['contactPhone']

                newUser = request.user
                newUser.abstractuser.name = new_name
                newUser.abstractuser.web_page = new_webpage
                newUser.abstractuser.contact_phone = new_contact_phone

                newUser.abstractuser.profile_image = request.FILES['file']
                newUser.save()
                newUser.abstractuser.save()
                return redirect('/company')
            return redirect('/company')
        else:
            return render(request, 'company/company.html',
                          {'user': request.user.abstractuser, 'vacancies': request.user.abstractuser.vacancies.all()})


@login_required
def company_add_vacancy(request):
    vform = VacancyForm()
    tform = TaskForm()
    if (request.method == "POST"):
        vform = VacancyForm(request.POST)
        tform = TaskForm(request.POST)

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
        '''
        vacancy_name = request.POST['vacancy_name']
        vacancy_comment = request.POST['vacancy_comment']
        vacancy_description = request.POST['vacancy_description']
        vacancy_salary = request.POST['vacancy_salary']

        task_name = request.POST['vacancy_name']
        task_description = request.POST['vacancy_description']
        task_salary = request.POST['vacancy_salary']
        task_email
        '''
    data = {'vform':vform, 'tform':tform}
    return render(request, 'company/company_add_vacancy.html', data)


@login_required
def company_delete_vacancy(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    print(vacancy.name)
    print("ok")
    print(request.method)
    if request.method == 'POST':
        print("Got in!")
        request.user.abstractuser.vacancies.remove(vacancy)
        vacancy.delete()
        request.user.abstractuser.save()
        print(vacancy.name)
    return redirect("/company")
