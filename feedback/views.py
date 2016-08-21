from django.shortcuts import render
from feedback.models import Feedback
from django.shortcuts import redirect
# Create your views here.

def send_feedback_view(request):
    if request.method == "POST":
        sender_email = request.POST['email']
        text = request.POST['text']
        feedback = Feedback()
        feedback.sender_email = sender_email
        feedback.text = text
        feedback.save()
    return redirect('index')

def feedback_view(request):
    return render(request, 'feedback/feedback.html')
