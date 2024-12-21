from django.shortcuts import render

def search_web(request):
    return render(request, 'Search_web.html')