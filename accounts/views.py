from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.exceptions import ValidationError

# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get( username = request.POST['username1'])
                return render(request,'accounts/signup.html', {'error':'Username hs already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST.get('username1') , password = request.POST.get('password1') )
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request,'accounts/signup.html', {'error':'Password Must Match'})

    else:
        #return render(request,'accounts/signup.html', {'error':'Password Must Match'})
        return render(request, 'accounts/signup.html')






def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username1'],password=request.POST['password1'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html',{'error':'Invalid Username or Paasword.'})

    
    return render(request, 'accounts/login.html')





def logout(request):
    #to be done later
    if request.method =='POST':
        auth.logout(request)
        return redirect('home')
    


