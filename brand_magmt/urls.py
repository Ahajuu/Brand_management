from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name="home"),
    path('dashboard/', views.dashboard,name="dashboard"),
    path('products/', views.products,name="products"),
    path('designers/', views.designers,name="designers"),
    path('market/', views.market,name="market"),
    path('requests/', views.requests,name="requests"),
    path('settings/', views.settings,name="settings"),
    path('register/', views.register,name="register"),
    path('designers/profile/', views.profile,name="profile"),
    path('designers/dregister/', views.dregister,name="dregister"),
    
]