from django.shortcuts import render
from django.http import HttpResponse
from mis.forms import InStockForm

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
    return render(request, 'instock.html', {'f': f})

