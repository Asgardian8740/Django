from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
import subprocess
import master
# Create your views here.
def index(request):
    po=master.get_data()
    return HttpResponse(po)

def home(request):
    name=request.POST.get("username")
    return render(request, 'home.html')


def results(request):
    name = request.POST.get("username")
    print(name)
    res=master.get_data(name)

    is_bully = "isn't a CyberBully"
    if(res[0]=="Bully"):
        is_bully= "is a CyberBully"

    labels = []
    data = []
    labels.append("negative")
    labels.append("positive")
    labels.append("neutral")
    data.append(res[2])
    data.append(res[1])
    data.append(res[3])

    if request.method == "POST":
        username = request.POST['username']

    return render(request, 'results.html', {"username": username,
                                            "is_bully": is_bully,
                                            "labels": labels,
                                            "data": data})
