from django.shortcuts import render
# Create your views here.
def learn_python(request):
    return render(request,'app1/home.html')