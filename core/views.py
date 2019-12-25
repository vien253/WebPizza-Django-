from django.shortcuts import render,redirect
from  django.views import View
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import SanPham
# Create your views here.

class HomeView(View):
    def get(self,request):
        sp = SanPham.objects.all()
        context = {"sp": sp}
        return render(request,'homepage/index.html',context)          
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
        return render(request,template_name='homepage/appertizer.html')  
class drinkView(View):
    def get(self,request):
        return render(request,template_name='homepage/drink.html')  
class pizzaView(View):
    def get(self,request):
        return render(request,template_name='homepage/pizza.html')
class pastaView(View):
    def get(self,request):
        return render(request,template_name='homepage/pasta.html')    
          
