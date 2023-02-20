from django.shortcuts import render, reverse

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Member
# def members(request):
#     a= "myfirst.html"
#     return render (request,'myfirst.html',{'a':a})
    #template = loader.get_template('myfirst.html')
    #return HttpResponse(template.render())
    #return HttpResponse("Hello world!")

def members(request):
  mymembers = Member.objects.all().values()
#   template = loader.get_template('myfirst.html')
#   context = {
#     'mymembers': mymembers,
#   }
  #return HttpResponse(template.render(context, request))
  return render(request,'add.html', {'mymembers': mymembers})
def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  x = request.POST['first']
  y = request.POST['last']
  member = Member(firstname=x, lastname=y)
  member.save()
  return HttpResponseRedirect(reverse('members'))  
  
def addrecord(request):
      if request.method == 'POST':
        # firstname = 'priya'
        # lastname = 'patil'
        obj = members.objects.create(firstname = 'priya',
        lastname = 'patil')
        obj.save()
  

  