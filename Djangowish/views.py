from django.shortcuts import render

def Homepage(request):
    data = {}
    try:
        if request.method == "POST":
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            msg = request.POST.get('msg')
            song = request.POST.get('song')
            mn = bday(fname = fname,
                      lname = lname,
                      msg = msg,
                      song = song)
            mn.save()
    except:
        pass
        
    return render(request,"index.html")

def choice(request):
    return render(request, "choice.html")

def login(request):
    return render(request, "login.html")

def bdayInput(request):
    return render(request, "bdayinput.html")

def valentineInput(request):
    return render(request, "valentineinput.html")

def bday(request):
    return render(request, "index.html")

def vday(request):
    return render(request, "vday.html")