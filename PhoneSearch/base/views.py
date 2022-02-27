from pyexpat import features
from django.contrib import auth
from django.shortcuts import render
from .models import User, Phone, phoneName
from .forms import PhoneImage
from django.db.models import Q

# Create your views here.

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    phoneNamess = phoneName.objects.filter(
        Q(phoneName__icontains = q)
    )
    bodyPhoneName = Phone.objects.all()
    context = {'phoneNamess': phoneNamess, 'bodyPhoneName': bodyPhoneName}

    return render(request, 'base/main.html', context)
    #pass


def phoneInfo(request, pk):
    phones = phoneName.objects.get(id=pk)
    specifications = Phone.objects.get(id=pk)
    spec_loop = Phone.objects.filter(id=pk)
    context = {'phonest': phones, 'spec':specifications, 'spll':spec_loop}
    return render(request, 'base/phoneinfo.html', context)


def test(request):
    phones = Phone.objects.all()
    context = {'phones': phones}
    return render(request, 'base/test.html',context)
