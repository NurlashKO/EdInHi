from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from django.shortcuts import render, get_object_or_404, redirect

from company.models import Vacancy
from profile.forms import UploadFileForm


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

        else:
            return render(request, 'company/company.html',
                          {'user': request.user.abstractuser, 'vacancies': request.user.abstractuser.vacancies.all()})


class VacancyForm(ModelForm):
    class Meta:
        model = Vacancy
        fields = ['name', 'description', 'salary']


@login_required
def company_add_vacancy(request):
    form = VacancyForm(request.POST or None)
    if form.is_valid():
        vacancy = form.save(commit=False)
        vacancy.save()
        request.user.abstractuser.vacancies.add(vacancy)
        request.user.abstractuser.save()
        print(vacancy.name)
        return render(request, 'company/company.html',
                      {'user': request.user.abstractuser, 'vacancies': request.user.abstractuser.vacancies.all()})
    return render(request, 'company/company_add_vacancy.html', {'form': form})


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
        return redirect("company")
    return render(request, 'company/company_delete_vacancy.html', pk)
