from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
#from django.contrib.auth.models import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

from django.http import HttpResponse
from .models import Employee

# Create your views here.
def allemployees(request):
    emp = Employee.objects.all()
    return render(request, "emp/allemployees.html", {"allemployees": emp })

def singleemployee(request, empid):
    return render(request, "emp/singleemployee.html")

def addemployee(request):
    if request.method == 'POST':
        #take all the paramaters from their nasmes kept.
        employeeid = request.POST.get('employeeid')
        employeename = request.POST.get('employeename')
        employeeemail = request.POST.get('employeeemail')
        employeeaddress = request.POST.get('employeeaddress')
        employeephone = request.POST.get('employeephone')
        
        #create an object of the employee model.
        e = Employee()
        e.employeeid = employeeid
        e.employeename = employeename
        e.email = employeeemail
        e.address= employeeaddress
        e.phone = employeephone
        
        e.save() 
        return redirect("/allemployees")
       # return HttpResponse("/allemployees")
        
    return render(request, "emp/addemployee.html" )

def deleteemployee(request,empid):
    e = Employee.objects.get(pk = empid)
    e.delete()
    return redirect("allemployees")
    
def updateemployee(request,empid):
    e = Employee.objects.get(pk = empid)
    e=Employee(request.POST,)
   
    #return redirect("allemployees")
    return render(request, "emp/updateemployee.html", {"singleemp": e})

def doupdateemployee(request,empid):
    updatedemployeeid      = request.POST.get('employeeid')
    updatedemployeename    = request.POST.get('employeename')
    updatedemployeeemail   = request.POST.get('employeeemail')
    updatedemployeeaddress = request.POST.get('employeeaddress')
    updatedemployeephone   = request.POST.get('employeephone')
    
    
    emp = Employee.objects.get(pk = empid)
    
    emp.employeeid   = updatedemployeeid
    emp.employeename = updatedemployeename
    emp.email        = updatedemployeeemail
    emp.address      = updatedemployeeaddress
    emp.phone        = updatedemployeephone
    emp.save()
    return redirect("allemployees")
def index(request):
    return render(request, "user/index.html", {"title": "index"})


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST) or None
        if form.is_valid():
            username = request.POST.get("username")
            #########################mail####################################
            htmly = get_template("user/Email.html")
            d = {"username": username}
            subject, from_email, to = "hello", "from@example.com", "to@emaple.com"
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            try:
                msg.send()
            except:
                print("error in sending mail")
            ##################################################################
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Your account has been created! You are now able to log in"
            )
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(
        request, "user/register.html", {"form": form, "title": "reqister here"}
    )


###################################################################################
################login forms###################################################


def Login(request):
    if request.method == "POST":
        # AuthenticationForm_can_also_be_used__

        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f" wecome {username} !!")
            return redirect("index")
        else:
            messages.info(request, f"account does not exit plz sign in")
    form = AuthenticationForm()
    return render(request, "user/login.html", {"form": form, "title": "log in"})