from vt1.settings import BASE_DIR, MEDIA_ROOT
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage

from pathlib import Path
import os


import requests
import sys
from subprocess import run,PIPE
import requests

from AudioAnalyzer import *
import random
import colorsys

import math

import matplotlib
import matplotlib.pyplot as plt
import librosa.display
import numpy as np



import pygame

# Create your views here.
context={}
c={}
def upload(request):
    
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        c['filename']=uploaded_file.name
        context['url'] = fs.url(name)
        
    return render(request, 'upload.html', context)

def external(request):
    inp= request.POST.get('param')
    s=context['url']

    # print(c['filename'])
    q=c['filename']
    d="file_name="
    a=d+"\""+s+"\""
    # a=d+s+'/'+q
    print(a)

    mr=MEDIA_ROOT+'\\'+q
    print(mr)
    mra=d+"\""+mr+"\""

    # with open("main.py", "r+") as file:
    #     file.write(mra)
    #     file.write("\n")
    #     file.seek(0)
    
    # print(s)
    # t=os.path.join(BASE_DIR,s)
    # print(t)
    # print(BASE_DIR)


    
    # m=os.path.dirname(MEDIA_ROOT,s)
    # print(m)
    out= run([sys.executable,'C://Users//umark//myprojects//vt1//main.py',inp],shell=False,stdout=PIPE)
    print(out)
    return render(request,'upload.html',{'data1':out.stdout})