from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
#from django.template import loader

def members(request):
    a= "myfirst.html"
    return render (request,'myfirst.html',{'a':a})
    #template = loader.get_template('myfirst.html')
    #return HttpResponse(template.render())
    #return HttpResponse("Hello world!")
