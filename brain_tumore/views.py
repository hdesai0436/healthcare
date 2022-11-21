from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .apps import BrainTumoreConfig
import cv2
import numpy as np
import os
import pathlib


parent_file = pathlib.Path().resolve()

# Create your views here.
def index(request):
    return render(request,'home.html')

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        
        
        
        
        pic = cv2.imread(str(pathlib.Path.joinpath(parent_file,'media',filename)))
        openimages = cv2.cvtColor(np.array(pic), cv2.COLOR_RGB2BGR)
        imgs = cv2.resize(openimages,(224,224))
        imgs = imgs.reshape(1,224,224,3)
        predication_model = np.argmax(BrainTumoreConfig.model.predict(imgs))
        if predication_model == 0:
            result = 'Model did not detect Tumore in the Picture.'
        else:
            result = 'Model Detect Tumore in the Picture.Please see doctor for Treatment'
        return render(request, 'brain_tumore.html', {
            'uploaded_file_url': uploaded_file_url,
            'result':result
        })

    return render(request, 'brain_tumore.html')