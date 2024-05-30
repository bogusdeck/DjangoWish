# urls.py
from django.urls import path, include
from .views import  home, breath, Rizz, letter, proposal,memories,bubblewrap,photogif,Bie


urlpatterns = [
    path('vdayinput/',vdayinput, name="vdayinput"),
    path('In/',home, name="home"),
    path('In-your/',breath, name="breath"),
    path('In-your-eyes/',Rizz, name="Rizz"),
    path('In-your-eyes-I/',letter, name="letter"),
    path('In-your-eyes-I-find/',proposal, name="proposal"),
    path('In-your-eyes-I-find-my/', memories,name="memories"),
    path('In-your-eyes-I-find-my-forever/', bubblewrap,name="bubblewrap"),
    path('In-your-eyes-I-find-my-forever-and/', photogif,name="photogif"),
    path('In-your-eyes-I-find-my-forever-and-always/', Bie,name="Bie"),
]


# "In your eyes, I find my forever and always."