from django.shortcuts import render

# Create your views here.
def get_bg_signin(request):
    return render(request, 'borgagarden_signin/bg_signin.html')

