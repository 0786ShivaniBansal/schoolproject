from django.shortcuts import render

from school.models import student,Book,Bookinv

# Create your views here.
def reg(request):
    if(request.method=='POST'):
        print(request.POST)
        s=student.objects.create(firstname=request.POST['firstname'],lastname=request.POST['lastname'],address=request.POST['address'],city=request.POST['city'],state=request.POST['state'],emailaddress=request.POST['emailaddress'],phone=request.POST['phone'],DOB=request.POST['DOB'],gender=request.POST['gender'],mothersname=request.POST['mothersname'],fathersname=request.POST['fathersname'],fatheroccupation=request.POST['fatheroccupation'])
    return render(request,'studentreg.html')

def books(request):
    if(request.method=='POST'):
        print(request.POST)
        b=Book.objects.create(title=request.POST['title'],author=request.POST['author'],isbn=request.POST['isbn'])
    return render(request,'books.html')

def bookinv(request):
    if(request.method=='POST'):
        print(request.POST)
        i=Bookinv.objects.create(Title=request.POST['Title'],Author=request.POST['Author'],ISBN=request.POST['ISBN'],Publisher=request.POST['Publisher'],year=request.POST['year'])
    return render(request,'bookinv.HTML')