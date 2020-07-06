"""IgCrm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path, include

from app01 import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/',include('tinymce.urls') ),
    path('login/', views.login),
    path('get_valid_img/', views.get_valid_img),
    path('reg/', views.reg),
    path('logout/', views.logout),
    path('index/', views.index),
    path('', views.index),
    path('customers/list/', views.CustomerView.as_view(),name="customers_list"),
    path('mycustomers/', views.CustomerView.as_view(),name="mycustomers"),
    path('customer/add/', views.AddEditCustomerView.as_view(),name="addcustomers"),
    re_path('customer/edit/(\d+)', views.AddEditCustomerView.as_view(),name="editcustomers"),
    path('consult_records/', views.ConsultRecordView.as_view(),name="consult_records"),
    path('consult_records/add/', views.AddEditConsultRecordView.as_view(), name="add_consult_records"),
    re_path('consult_records/edit/(\d+)', views.AddEditConsultRecordView.as_view(), name="edit_consult_records"),
]
