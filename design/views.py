from django.shortcuts import render
from design.models import form

# Create your views here.
def design(request):
    if(request.method=='POST'):
        print(request.POST)
        f=form.objects.create(emailaddress=request.POST['emailaddress'],password=request.POST['password'])
    return render(request,'create.html')

