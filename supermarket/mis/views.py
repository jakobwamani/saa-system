from django.shortcuts import render
from django.http import HttpResponse
from mis.forms import InStockForm

def index(request):
    return HttpResponse("Hello,Sarah and Aidah.")

def instocking(request):
    # # Create a form instance with POST data.
    # >>> f = AuthorForm(request.POST)
    # # Create, but don't save the new author instance.
    # >>> new_author = f.save(commit=False)
    # # Modify the author in some way.
    # >>> new_author.some_field = 'some_value'
    # #Save the new instance.
    # >>> new_author.save()
    # # Now, save the many-to-many data for the form.
    # >>> f.save_m2m()
    if request.method == 'POST':
        f = InStockForm(request.POST)
        if f.is_valid():
            new_data=f.save(commit=False)
            new_data.save()
            return HttpResponse("Thanks")
    else:
        f = InStockForm()
    return render(request, 'instock.html', {'f': f})

