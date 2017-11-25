from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    my_dict = {"inserted_value" : "Done by myself"}
    return render(request, 'AppTwo/index.html', context = my_dict)

def help(request):
    info_dict = {"help_info": "this is very useful tip..."}
    return render(request, 'AppTwo/help.html', context = info_dict)
