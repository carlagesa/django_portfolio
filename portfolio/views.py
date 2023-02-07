from django.shortcuts import render
from portfolio.models import PreviousWork
from . import forms
from portfolio.forms import NewContact
# Create your views here.

def index(request):
    index = NewContact()

    if request.method == 'POST':
        index = NewContact(request.POST)

        if index.is_valid():
            index.save(commit=True)
            # return index(request)
        else:
            print('ERROR FORM INVALID')
    return render(request, 'portfolio/index.html', {'form':index})
    

def access(request):
    work_list = PreviousWork.objects.all()
    # work_dict = {'access_records':work_list}
    return render(request, 'portfolio/index.html', {'work_list': work_list})
