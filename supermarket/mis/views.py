from django.shortcuts import render
from django.http import HttpResponse
from mis.forms import InStockForm,SearchForm
from mis.models import stock
import cv2
from imutils.video import VideoStream

def index(request):
    return render(request,'index.html',{})

def instocking(request):
    if request.method == 'POST':
        f = InStockForm(request.POST)
        if f.is_valid():
            new_data=f.save(commit=False)
            new_data.save()
            return HttpResponse("Thanks")
        else:
            f = InStockForm()
    else:
        f = InStockForm()
    
    return render(request, 'instock.html', {'f': f})

def selling(request):
    
    cv2.namedWindow("preview")
    vc = cv2.VideoCapture(0)

    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False

    while rval:
        cv2.imshow("preview", frame)
        rval, frame = vc.read()
        key = cv2.waitKey(20)
        if key == 27: # exit on ESC
            break
    cv2.destroyWindow("preview")
    return render(request,'selling.html',{})