from django.shortcuts import render
from django.http import HttpResponse
from .models import goovi_db
from .forms import goovi_form
def index(requests):
    if(requests.method == 'POST'):
        y = goovi_form(request.POST,request.FILES)
        if(goovi_form.isvalid()):
            x = goovi_db(name = goovi_form['name'],data = "test data",file = goovi_form['file'])
            x.save()
    else:
        form = goovi_form()
        context = {'form':form}
    return render(requests,"index.html",context)
