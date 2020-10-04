from django.http import request
from django.shortcuts import render

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, 'input_data.html')
    else:
        return render(request, 'login.html')

def past_data(request):
    return render(request, 'past_data.html')

def input_data(request):
    return render(request, 'input_data.html')