from django.urls import path
from . import views

urlpatterns=[
    path("",            views.allemployees, name="allemployees"),
    path("allemployees/", views.allemployees, name="allemployees"),
    #path('emp/', include('emp_management.urls')),  
    path("singleemployee/<int:empid>/", views.singleemployee, name="singleemployee"),
    path("addemployee/",                views.addemployee,    name="addemployee"),
    path("deleteemployee/<int:empid>/", views.deleteemployee,    name="deleteemployee"),
    path("updateemployee/<int:empid>/", views.updateemployee,    name="updateemployee"),
    path("doupdateemployee/<int:empid>/", views.doupdateemployee,    name="doupdateemployee"),
    #path('login/', views.login_view, name='login'),
   # path('register/', views.register_view, name='register'),
   # path('', views.home_view, name='home'),
    path("", views.index, name="index"),

]