from django.shortcuts import render, get_object_or_404
from .models import Horoskop

# Create your views here.
def index(requests):

    queryset = Horoskop.objects.all()

    context = {
        'queryset': queryset
    }
    return render(requests, 'index.html', context)



def znak_detaljno(request, slug):

    detaljno = get_object_or_404(Horoskop, slug=slug)

    context = {
        'detaljno': detaljno,
    }
    return render(request, 'znak-detaljno.html', context)
