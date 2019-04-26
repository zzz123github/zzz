from django.shortcuts import render
from .pachong import get_title
from .models import mymodel

# Create your views here.
def xianshi(request):
    movies = get_title()

    if mymodel.objects.count() == 0:
        for each in movies:
            addition = mymodel(title=each['title'], actor=each['actor'])
            addition.save()

    data = mymodel.objects
    return render(request, 'zzz.html', {'data': data})