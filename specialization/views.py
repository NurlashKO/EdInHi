from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from main_app.models import wishSpec
from specialization.models import Specialization


def all_specializations_view(request):
    all = Specialization.objects.all()
    return render(request, 'specialization/specializations.html', {'all': all})

def delete_from_wishlist(request, pk):
    specialization = get_object_or_404(Specialization, pk=pk)
    if(request.method=="POST"):
        wish_spec = get_object_or_404(wishSpec, wish_spec_id=pk)
        request.user.abstractuser.wishlist.remove(wish_spec)
        specialization.in_wishlist_of_users -= 1
        specialization.save()
        wish_spec.delete()
        request.user.abstractuser.save()
        print(request.user.abstractuser.wishlist.count())
    return redirect("/spec/" + str(pk))

def specialization_view(request, pk):
    specialization = get_object_or_404(Specialization, pk=pk)
    skills = specialization.skills.all()
    progress = 0
    if request.user.is_authenticated():
        if request.method == "POST":
            if(request.user.abstractuser.wishlist.filter(wish_spec_id=pk).exists()):
                print("You have it")
            else:
                wish_spec = wishSpec(wish_spec_id=int(pk))
                wish_spec.save()
                request.user.abstractuser.wishlist.add(wish_spec)
                request.user.abstractuser.save()
                specialization.in_wishlist_of_users+=1
                specialization.save()
        passed_skills = request.user.skill_set.all()
        passed = 0
        can_add_to_wishlist=request.user.abstractuser.wishlist.filter(wish_spec_id=pk).exists()
        for skill in skills:
            if skill in passed_skills:
                passed+=1
        progress = int(passed/specialization.skills.all().count() * 100)
    else:
            progress = 0
            passed_skills = None
    return render(request, 'specialization/specialization.html', {'passed_skills':passed_skills, 'specialization': specialization, 'progress': progress, "add" : can_add_to_wishlist,})
