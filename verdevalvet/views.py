from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index (request):
    return render(request, 'index.html')
def feedback(request):
    return render(request, 'feedback.html')
def events (request):
    return render(request, 'events.html')    
def checkout (request):
    return render(request, 'checkout.html')
def my_ticket (request):
    return render(request, 'form.html')
def contact (request):
    return render(request, 'contact.html')