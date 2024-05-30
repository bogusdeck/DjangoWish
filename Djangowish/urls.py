# urls.py
from django.urls import path, include
from django.contrib import admin
from .views import  choice, mylogout, bdayinput, vdayinput,login


urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('login/',login, name="login"),
    path('logout/', mylogout, name='logout'),
    path('vdayinput/',vdayinput, name="vdayinput"),
    path('bdayinput',bdayinput,name='bdayinput'),
    path('', choice, name='choice')
]
