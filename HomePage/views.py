from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import call_model

from .Forms import NameForm

# Create your views here.

def home_page(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            text=form.cleaned_data.get('Text')
            Sonuc=call_model(text)
            return render(request, 'HomePage.html', {'Sonuc':Sonuc})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'HomePage.html', {'form': form})