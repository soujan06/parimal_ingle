from django.shortcuts import render
from .models import Contacts
from .forms import ContactForm

def home(request):
    all_contacts = Contacts.objects.all
    return render(request, 'home.html', {'all_contacts': all_contacts})

def about(request):
    return render(request, 'about.html', {})

def addContact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_contacts = Contacts.objects.all
            return render(request, 'home.html', {'all_contacts': all_contacts})
    else:
        return render(request, 'addContact.html', {})

def details(request):
    return render(request, 'details.html', {})

def update(request):
    return render(request, 'update.html', {})

def deleteConf(request):
    return render(request, 'deleteConf.html', {})