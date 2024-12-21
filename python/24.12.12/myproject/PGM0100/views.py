from django.shortcuts import render
from bs4 import BeautifulSoup

# TODO : 크롤링해서 검색결과 보여줄것.


def search_web(request):
    return render(request, 'Search_web.html')
