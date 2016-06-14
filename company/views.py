from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from django.shortcuts import render

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
            return render(request, 'company/company.html', {'user': request.user.abstractuser, 'vacancies' : request.user.abstractuser.vacancies.all()})


class VacancyForm(ModelForm):
    class Meta:
        model = Vacancy
        fields = ['name', 'description', 'salary']

@login_required
def company_add_task(request):
    form = VacancyForm(request.POST or None)
    if form.is_valid():
        vacancy = form.save(commit=False)
        vacancy.save()
        request.user.abstractuser.vacancies.add(vacancy)
        request.user.abstractuser.save()
        print(vacancy.name)

    return render(request, 'company/company_add_task.html', {'form': form})
