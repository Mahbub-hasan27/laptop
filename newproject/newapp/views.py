from django.shortcuts import render,redirect
from .models import BannerSlider, CardInfo,SignUp

# Create your views here.
def home(request):
    banners=BannerSlider.objects.all()
    cards=CardInfo.objects.all()
     
    context={
        'banners':banners,
        'cards':cards
    }


    return render(request,'home.html',context)

def signup(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        repeatpassword=request.POST['repeatpassword']

        submit=SignUp(name=name,email=email,password=password)
        submit.save()
        return redirect('signup')
        
    return render(request,'signup.html')


def login(request):
    
    return render(request,'login.html')

    
   


