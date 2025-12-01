from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse

def status_view(request):
    data = {
        "status": "ok",
        "version": "1.0.0"
    }
    return JsonResponse(data)

def hello_view(request):
    return HttpResponse("Hello, Django!")

def new_view(request):
    return render(request, "win.html")
def template_view(request):
    context = {"name": "Dhinesh"}
    return render(request, "hello.html", context)
