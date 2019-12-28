from django.shortcuts import render,redirect
from  django.views import View
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from core.models import SanPham
from core.forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm
# Create your views here.



# Create your views here.

class HomeView(View):
    def get(self,request):
        sp = SanPham.objects.all()
        context = {"sp": sp}
        return render(request,'homepage/index.html',context)   
class dangkyView(View):
    def get(self,request):
        form =SignUpForm()
        context = {'form': form}
        return render(request, 'homepage/dangky.html',context)    
    def post(self,request):
        """Register a new user."""
        # Process completed form.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to home page.
            login(request, new_user)
            return redirect('index')
        # Display a blink or invalid form
        context = {'form': form}
        return render(request, 'homepage/dangky.html', context)

class loginView(View):
    def get(self,request):
        return render(request, 'homepage/login.html')
    
    def post(self, request):
        tai_khoan = request.POST.get('un')
        mat_khau = request.POST.get('pass')
        my_user = authenticate(username = tai_khoan, password = mat_khau)
        if my_user is None:
            return render(request, 'homepage/login.html',{'name': "Đăng nhập sai!"})           
        login(request, my_user)
        return redirect('index')
class logoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

class appertizerView(View):
    def get(self,request):
        sp1 = SanPham.objects.all()
        context = {"sp": sp1}
        return render(request,'homepage/appertizer.html',context)  
class drinkView(View):
    def get(self,request):
        sp1 = SanPham.objects.all()
        context = {"sp": sp1}
        return render(request,'homepage/drink.html',context)  
class pizzaView(View):
    def get(self,request):
        sp1 = SanPham.objects.all()
        context = {"sp": sp1} 
        return render(request,'homepage/pizza.html',context)
class pastaView(View):
    def get(self,request):
        sp1 = SanPham.objects.all()
        context = {"sp": sp1} 
        return render(request,'homepage/pasta.html',context)    
          
