from django.shortcuts import render

#1 page 4 words 
#rizz lines
#date you guyz met
#letter
#10 photos

def home(request):
    return render(request,'vday/1.html')

def breath(request):
    return render(request,'vday/2.html')

def Rizz(request):
    return render(request,'vday/3.html')

def letter(request):
    return render(request,"vday/4.html")

def proposal(request):
    return render(request,'vday/5.html')

def memories(request):
    return render(request,'vday/6.html')

def bubblewrap(request):
    return render(request,'vday/7.html')

def photogif(request):
    return render(request,'vday/8.html')

def Bie(request):
    return render(request,'vday/9.html')
