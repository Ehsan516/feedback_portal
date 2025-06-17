from django.shortcuts import render

# Create your views here.

def feedback_form(request):
    return render(request, 'core/feedback_form.html')