from django.shortcuts import render
import cv2
import numpy as np
import tensorflow as tf
import os
import pathlib
from django.core.files.storage import FileSystemStorage
from .apps import ChestConfig
# Create your views here.
parent_file = pathlib.Path().resolve()
def chest_predict(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        upload_file_url= fs.url(filename)
        pic = cv2.imread(str(pathlib.Path.joinpath(parent_file,'media',filename)))
        openimages=cv2.cvtColor(np.array(pic),cv2.COLOR_RGB2BGR)
        imgs=cv2.resize(openimages,(224,224))
        imgs=imgs.reshape(1,224,224,3)
        chest_pred = np.argmax(ChestConfig.chest_model.predict(imgs))
        if chest_pred == 0:
            chest_result = 'Model detected Covid in the Lung'
        elif chest_pred == 1:
            chest_result = 'Model detected Lung Obesity '
        elif chest_pred == 2:
            chest_result = "Model didn't detected in the Lung. (Normal Lung)"
        elif chest_pred == 3:
            chest_result = 'Model detected viral pneumonia in the Lung'
        elif chest_pred == 4:
            chest_result = "Model detected Tb  in the Lung"

        return render(request,'chest.html',
        {   'uploaded_file_url':upload_file_url,
            'chest_result':chest_result
        })


    return render(request,'chest.html')