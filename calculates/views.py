from django.shortcuts import render

def index(request):
    """The home page for my Calculator"""
    return render(request, 'calculates/index.html')
