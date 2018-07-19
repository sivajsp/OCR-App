from django.shortcuts import render
from django.http import HttpResponse
from .models import goovi_db
from .forms import goovi_form
import io
import os
from google.cloud import vision
from google.cloud.vision import types
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def goovi_api(filename):
    client = vision.ImageAnnotatorClient()
    with io.open(filename,'rb') as image_file:
        content = image_file.read()
    image = types.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    data = 'Texts:'
    for text in texts:
        data+=text.description+" "

def index(request):
    if(request.method == 'POST'):
        y = goovi_form(request.POST,request.FILES)
        if(y.is_valid()):
            x = goovi_db()
            x.name = y.cleaned_data["name"]
            x.file = y.cleaned_data["file"]
            x.data = "test data"
            x.save()
            print(goovi_api(BASE_DIR+"/goovi/"+goovi_db.objects.get(name=y.cleaned_data["name"]).file.url))
        context = {'form':y,'data':"data"}
    else:
        form = goovi_form()
        context = {'form':form}
    return render(request,"index.html",context)
