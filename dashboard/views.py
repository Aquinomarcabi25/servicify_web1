from django.shortcuts import render


# Create your views here.
def dashboard(request):
    return render(request, 'includes/dashboard.html')


def login(request):
    return render(request, 'includes/login.html')


def register(request):
    return render(request, 'includes/register.html')
    
def workoffer(request):
    return render(request, 'includes/workoffer.html')
    
def workoffer2(request):
    return render(request, 'includes/workoffer2.html') 

def acquireservice(request):
    return render(request, 'includes/acquireservice.html') 

def acquireservice2(request):
    return render(request, 'includes/acquireservice2.html') 

def errorpage(request):
    return render(request, 'includes/errorpage.html') 

def contactus(request):
    return render(request, 'includes/contactus.html') 

def aboutus(request):
    return render(request, 'includes/aboutus.html') 
