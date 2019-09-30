from django.core.files.storage import FileSystemStorage
from django.shortcuts import render ,HttpResponse,redirect
from firstapp.forms import userDataForm
from django.contrib.auth.hashers import make_password,check_password
from firstapp.models import userData

# Create your views here.
def index(request):
    return HttpResponse("<h1>Welcome to First Response</h1>")
def home (request):
    return render(request,"home.html")
def about(request):

        n1="Vishal"
        names={"Vishal","kunal","Amit"}
        return render(request,"about.html",
                      {'n':n1,'l':names})
def index1(request):
    return render(request,'base1.html')

def index2(request):
    if request.method=="POST":
        form = userDataForm(request.POST)
        f = form.save(commit=False)
        user_image = None
        try:
            if request.FILES["userimage"]:
                my_files=request.FILES["userimage"]
                fs=FileSystemStorage()
                file_name=fs.save(my_files.name,my_files)
                user_image=fs.url(file_name)
                user_image=my_files.name
        except:
            pass

        f.userName=request.POST["username"]
        f.userPassword=make_password(request.POST["userpassword"])
        f.userEmail = request.POST["useremail"]
        f.userImage= user_image
        f.isActive=True
        f.save()
        return render(request,'form.html',{'sucess':True})
    return render(request,'form.html',{"sucess":True})

def updatefunction(request):
    if request.method=="POST":
        useremail=request.POST["useremail"]
        npassword=request.POST["userpassword"]
        username=request.POST["username"]
        userid=request.POST["userid"]

        updatedata=userData(userID=userid,userEmail=useremail,userPassword=npassword,userName=username)
        updatedata.save(update_fields=["userEmail","userPassword","userName"])
        return render(request,'udp.html',{"sucess":True})
    return render(request,'udp.html',{"sucess":True})

def datafetch(request):
    data=userData.objects.all()
    #data=userData.objects.filter(isActive=1)
    #data=userData.objects.get(userEmail="vishal20mandora@gmail.com")
    return render(request,'viewdata.html',{"d":data})


def deletedata(request):
    id=request.GET["id"]
    data=userData.objects.get(userID=id)
    data.delete()
    return redirect('/user/fetch/')


def editdata(request):
    id=request.GET["id"]
    data=userData.objects.get(userID=id)
    data.edit()
    return redirect('/user/fetch/')