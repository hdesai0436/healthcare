from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import cv2
import pathlib
from .apps import AlzheConfig
import numpy as np
parent_file = pathlib.Path().resolve()
# Create your views here.
def alz_pred(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name,myfile)
        upload_file_url = fs.url(filename)
        pic = cv2.imread(str(pathlib.Path.joinpath(parent_file,'media',filename)))
        openimages=cv2.cvtColor(np.array(pic),cv2.COLOR_RGB2BGR)
        imgs=cv2.resize(openimages,(224,224))
        imgs=imgs.reshape(1,224,224,3)
        alz_pred=np.argmax(AlzheConfig.alz_pred(imgs))
        
        if alz_pred == 0:
            result = 'Model Predict VeryMildDemented alzheimer'
        elif alz_pred == 1:
            result ='Model Predict ModerateDemented alzheimer'
        elif alz_pred == 2:
            result ='Model Predict MildDemented alzheimer'
        elif alz_pred == 3:
            result ='Model Predict NonDemented alzheimer'
            return render(request,'alz.html',
            {'upload_file_url':upload_file_url,
            'alz_result':result}
            )
    return render(request,'alz.html')