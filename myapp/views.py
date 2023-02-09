from django.shortcuts import render
from django.http import HttpResponse
import datetime


def index(request):
    now = datetime.datetime.now()
    context = {
        'message': 'Hello World!',
        'current_date': now,
    }
    return render(request, 'myapp/index.html', context)

def success_view(request):
    return render(request, 'myapp/success_view.html')

from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_form_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Pobierz dane z formularza i przetwórz je
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # form.save() zapisuje dane w bazie danych:
            form.save()
            return redirect('success_view')
    else:
        form = ContactForm()

    context = {'form': form}
    return render(request, 'myapp/contact_form.html', context)