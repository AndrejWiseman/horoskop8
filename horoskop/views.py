from django.shortcuts import render, get_object_or_404
from .models import Horoskop
from .utils import dnevni_horoskop, nedeljni_horoskop, mesecni_horoskop, godisnji_horoskop

# Create your views here.
def index(requests):

    queryset = Horoskop.objects.all()

    context = {
        'queryset': queryset
    }
    return render(requests, 'index.html', context)



# def horoskop_view(request, znak):
#     if znak == 'ovan':
#         dnevni = dnevni_horoskop(znak)
#         nedeljni = nedeljni_horoskop(znak)
#         mesecni = mesecni_horoskop(znak)
#         godisnji = godisnji_horoskop(znak)
#     elif znak == 'bik':
#         dnevni = dnevni_horoskop(znak)
#         nedeljni = nedeljni_horoskop(znak)
#         mesecni = mesecni_horoskop(znak)
#         godisnji = godisnji_horoskop(znak)
#     elif znak == 'blizanci':
#         dnevni = dnevni_horoskop(znak)
#         nedeljni = nedeljni_horoskop(znak)
#         mesecni = mesecni_horoskop(znak)
#         godisnji = godisnji_horoskop(znak)
#     elif znak == 'rak':
#         dnevni = dnevni_horoskop(znak)
#         nedeljni = nedeljni_horoskop(znak)
#         mesecni = mesecni_horoskop(znak)
#         godisnji = godisnji_horoskop(znak)
#     elif znak == 'lav':
#         dnevni = dnevni_horoskop(znak)
#         nedeljni = nedeljni_horoskop(znak)
#         mesecni = mesecni_horoskop(znak)
#         godisnji = godisnji_horoskop(znak)
#     elif znak == 'devica':
#         dnevni = dnevni_horoskop(znak)
#         nedeljni = nedeljni_horoskop(znak)
#         mesecni = mesecni_horoskop(znak)
#         godisnji = godisnji_horoskop(znak)
#     elif znak == 'vaga':
#         dnevni = dnevni_horoskop(znak)
#         nedeljni = nedeljni_horoskop(znak)
#         mesecni = mesecni_horoskop(znak)
#         godisnji = godisnji_horoskop(znak)
#     elif znak == 'skorpija':
#         dnevni = dnevni_horoskop(znak)
#         nedeljni = nedeljni_horoskop(znak)
#         mesecni = mesecni_horoskop(znak)
#         godisnji = godisnji_horoskop(znak)
#     elif znak == 'strelac':
#         dnevni = dnevni_horoskop(znak)
#         nedeljni = nedeljni_horoskop(znak)
#         mesecni = mesecni_horoskop(znak)
#         godisnji = godisnji_horoskop(znak)
#     elif znak == 'jarac':
#         dnevni = dnevni_horoskop(znak)
#         nedeljni = nedeljni_horoskop(znak)
#         mesecni = mesecni_horoskop(znak)
#         godisnji = godisnji_horoskop(znak)
#     elif znak == 'vodolija':
#         dnevni = dnevni_horoskop(znak)
#         nedeljni = nedeljni_horoskop(znak)
#         mesecni = mesecni_horoskop(znak)
#         godisnji = godisnji_horoskop(znak)
#     elif znak == 'ribe':
#         dnevni = dnevni_horoskop(znak)
#         nedeljni = nedeljni_horoskop(znak)
#         mesecni = mesecni_horoskop(znak)
#         godisnji = godisnji_horoskop(znak)
#
#
#     horoskop, created = Horoskop.objects.get_or_create(
#         znak=znak,
#         dnevni=dnevni,
#         nedeljni=nedeljni,
#         mesecni=mesecni,
#         godisnji=godisnji
#     )
#
#     return render(request, 'znak-detaljno.html', {
#         # 'znak': znak,
#         # 'dnevni': dnevni,
#         # 'nedeljni': nedeljni,
#         # 'mesecni': mesecni,
#         # 'godisnji': godisnji,
#
#         'horoskop': horoskop,
#     })



def znak_detaljno(request, slug):

    detaljno = get_object_or_404(Horoskop, slug=slug)

    context = {
        'detaljno': detaljno,
    }
    return render(request, 'znak-detaljno.html', context)
