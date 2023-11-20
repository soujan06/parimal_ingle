from django.shortcuts import render, redirect
from .models import Contacts
from .forms import ContactForm
from django.contrib import messages
from datetime import datetime

def update_time():
    created_time = datetime.now().strftime('%b %d, %Y, %H:%M')
    return created_time


def home(request):
    all_contacts = Contacts.objects.all()
    return render(request, 'home.html', {'all_contacts': all_contacts})

def about(request):
    return render(request, 'about.html', {})

def addContact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            print(form["contact_email"].value())
            if Contacts.objects.filter(contact_email=form['contact_email'].value()):
                messages.success(request, ('Contact with this E-mail id already exists! Unable to add contact.'))
                return redirect('addContact')
            else:
                form.save()
                messages.success(request, ('Contact created successfully.'))
                return redirect('home')
    else:
        return render(request, 'addContact.html', {'created_time': update_time()})

def details(request, contact_id):
    curr_contact = Contacts.objects.get(pk=contact_id)
    print(curr_contact)
    return render(request, 'details.html', {'curr_contact': curr_contact})

def update(request, contact_id):
    if request.method == 'POST':
        curr_contact = Contacts.objects.get(pk=contact_id)
        form = ContactForm(request.POST or None, instance=curr_contact)
        print(curr_contact.contact_notes)
        curr_name = curr_contact.contact_name
        curr_email = curr_contact.contact_email
        curr_notes = curr_contact.contact_notes
        if form.is_valid():
            print(form["contact_name"].value(), curr_contact.contact_name)
            print(form["contact_email"].value(), curr_contact.contact_email)
            print(form["contact_notes"].value(), curr_contact.contact_notes)
            if Contacts.objects.filter(contact_email=form['contact_email'].value(), contact_name=form['contact_name'].value(), contact_notes=form['contact_notes'].value()):
                messages.success(request, ('Contact already exists! No fields were modified by the user. No updates were made.'))
                return redirect('home')
            elif curr_email == form['contact_email'].value(): #Contacts.objects.filter(contact_email=form['contact_email'].value()) and (curr_name != form['contact_name'].value() or curr_notes != form['contact_notes'].value()):
                form.save()
                messages.success(request, ('Contact has been successfully updated'))
                return redirect('home')
            elif Contacts.objects.filter(contact_email=form['contact_email'].value()):
                messages.success(request, ('Other Contact with this same E-mail id already exists! Unable to update contact.'))
                return render(request, 'update.html', {'curr_contact': curr_contact, 'created_time': curr_contact.created_time})
            else:
                form.save()
                messages.success(request, ('Contact has been successfully updated'))
                return redirect('home')
    else:
        curr_contact = Contacts.objects.get(pk=contact_id)
        return render(request, 'update.html', {'curr_contact': curr_contact, 'created_time': update_time()})

def deleteConf(request, contact_id):
    curr_contact = Contacts.objects.get(pk=contact_id)
    return render(request, 'deleteConf.html', {'curr_contact': curr_contact})

def delete(request, contact_id):
    curr_contact = Contacts.objects.get(pk=contact_id)
    curr_contact.delete()
    return redirect('home')