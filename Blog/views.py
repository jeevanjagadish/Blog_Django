from django.http import HttpResponse
from django.shortcuts import render

def Homepage(request):
    #return HttpResponse('Homepage')
    return render(request,'Homepage.html')

def About(request):
   # return HttpResponse('About')
   return render(request,'About.html')
