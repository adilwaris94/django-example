from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from myapp.forms import FormName,SignupForm,userform,UserProfileInfoForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
from myapp.models import WebPage,Topic,AccessRecord,User_pro
def index(request):
    t=Topic.objects.order_by('top_name')
    Acc=AccessRecord.objects.order_by('date')
    my_dict={'topics':t,'access':Acc}
    return render(request,'myapp/index.html',context=my_dict)

def contact(request):
    return render(request,'myapp/contact.html',context=None)
def about(request):
    return HttpResponse('<h1>About Page</h1>')

def user(request):
    us=User_pro.objects.order_by('email')
    my_dict={'Users':us}

    return render(request,'myapp/user.html',context=my_dict)

def form_view(request):
    form=FormName()
    if request.method=="POST":
        form=FormName(request.POST)
        if form.is_valid():
            print("form submitted sucess")
            print("name: "+ form.cleaned_data['name'])

    return render(request, 'myapp/form_page.html',{'form':form})

def signup(request):
        form=SignupForm()
        if request.method=="POST":
            form=SignupForm(request.POST)
            if form.is_valid():
                form.save(commit=True)
                return index(request)
            else:
                print("There is an error")

        return render(request, 'myapp/signup.html',{'form':form})

def Register(request):
        registered=False
        user_form=userform()
        profile_form=UserProfileInfoForm()
        if request.method=="POST":
            print("Request post")
            user_form=userform(request.POST)
            profile_form=UserProfileInfoForm(request.POST)
            #print(request.POST['portfolio_site'])
            #print(request.POST['profile_pic'])
            #print(request.FILES['profile_pic'])
            print(profile_form.is_valid())
            if user_form.is_valid() and profile_form.is_valid:
                user=user_form.save()
                user.set_password(user.password)
                user.save()
                profile=profile_form.save(commit=False)
                profile.user=user
                if 'profile_pic' in request.FILES:
                    profile.profile_pic=request.FILES['profile_pic']
                    profile.save()
                    registered=True
                return render(request, 'myapp/index.html',{'registered':registered})
            else:
              print("There is an error")
              print(user_form.errors,profile_form.errors)
        else:
            print("Request is not post")

        return render(request, 'myapp/register.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})
def user_login(request):
    print('hello')
    if request.method=='POST':
        Username=request.POST.get('uname','')

        Password=request.POST.get('psw','')
        print(Username,Password)
        user=authenticate(username=Username,password=Password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('myapp:index'))
            else:
                print("there is some  tried to login error in login")
                print("Username {} and password {}".format(Username, Password))
                return HttpResponse("in valid login details")
    else:
        return render(request, "myapp/login.html",{})

@login_required
def special(request):
    return HttpResponse("you are loged in")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("myapp:index"))
