from django.shortcuts import render, HttpResponse

# Create your views here.

def test_view(request):
    return HttpResponse("First view is working")

def html_view(request):
    return render(request, "base.html")