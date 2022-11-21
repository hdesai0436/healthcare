from django.shortcuts import render
from .apps import PolypsConfig
from django.core.files.storage import FileSystemStorage
import cv2
import pathlib
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from skimage import io
parent_file = pathlib.Path().resolve()
# Create your views here.

def polyps_predication(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        upload_file_ulr = fs.url(filename)

        
        img = io.imread(str(pathlib.Path.joinpath(parent_file,'media',filename)))
        img = cv2.resize(img,(256,256))
        img = np.array(img,dtype=np.float64)
        img -= img.mean()
        img /= img.std()
        x = np.empty((1,256,256,3))
        x[0,] = img
        pred = PolypsConfig.polyps_model(x)
        mask_pred = np.array(pred).squeeze().round()
        img[mask_pred !=0]=[0,255,0]
        plt.savefig(img,format='png')
        
        return render(request,'polyps.html',{
            'mask':mask_pred,
            'upload_file_url':upload_file_ulr,
            
        })


    return render(request,'polyps.html')