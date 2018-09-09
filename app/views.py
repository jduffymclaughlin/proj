from django.shortcuts import render



# Create your views here.

def index(request):
    return render(request, "app/index.html")

def services(request):
    return render(request, 'app/services.html')

def about_me(request):
    return render(request, 'app/about_me.html')

def contact(request):
    return render(request, 'app/contact.html')

def book_now(request):
    return render(request, 'app/book_now.html')
