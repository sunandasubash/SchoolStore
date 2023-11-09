from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from storeapp.form import  StudentForm


# Create your views here.
def home(request):
    return render(request,'index.html')

#store booking form
from django.shortcuts import render



def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('success')
            except:
                pass

    else:
        form = StudentForm()

    context = {
        'form': form,
    }
    return render(request, 'student_form.html', context)

#register
def register(request):
    if request.method =='POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['con_password']
        if password == confirm:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exist")
                return redirect('register')
            elif User.objects.filter(email= email).exists():
                messages.info(request,"Emailid already exist")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password,first_name=firstname,last_name=lastname,email=email)
                user.save();
        else:
            messages.info(request,"Password is not matched")
            return redirect('register')
        return redirect('login')

    return render(request,'register.html')

#login
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('form')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    return render(request,'login.html')

#logout
def logout(request):
    auth.logout(request)
    return redirect('/')

def success(request):
    return render(request, 'success.html')
