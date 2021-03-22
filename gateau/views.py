from django.shortcuts import render

# Create your views here.

from django import forms
from gateau.models import Gateau

def album_mixt(request):
    gateaux = Gateau.objects.all()
    return render(request, 'album_mixt.html',  {'gateaux': gateaux})

def album_test(request):
    gateaux = Gateau.objects.all()
    return render(request, 'album_test.html',  {'gateaux': gateaux})

def album(request):
    return render(request, 'album.html',)

def home(request):
    return render(request, 'home.html')


def iscription(request):
    return render(request, 'inscription.html')

class GateauForm(forms.Form):
    name = forms.CharField()
    photo = forms.ImageField()

def new_gateau(request):
    sauvegarde = False
    form = GateauForm(request.POST or None, request.FILES)
    if form.is_valid():
        gateau = Gateau()
        gateau.name = form.cleaned_data["name"]
        gateau.photo = form.cleaned_data["photo"]
        gateau.save()
        sauvegarde = True

    return render(request, 'GatForm.html', {
        'form': form,
        'sauvegarde': sauvegarde
    })

def voir_gateau(request):
    return render(
        request,
        'voir_gateau.html',
        {'gateaux': Gateau.objects.all()}
    )
