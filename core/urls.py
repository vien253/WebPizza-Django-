from django.urls import path
from .views import HomeView,loginView,logoutView,appertizerView,drinkView,pastaView,pizzaView
urlpatterns = [
    path('', HomeView.as_view(),name='index'),
    path('login/', loginView.as_view(),name='login'),
    path('logout/', logoutView.as_view(),name='logout'),
    path('appertizer/', appertizerView.as_view(),name='appertizer'),
    path('drink/', drinkView.as_view(),name='drink'),
    path('pizza/', pizzaView.as_view(),name='pizza'),
    path('pasta/', pastaView.as_view(),name='pasta'),
    

]