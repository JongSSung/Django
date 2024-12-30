from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import pandas as pd


# TODO : 크롤링해서 검색 결과 db에 저장.


def search_web(request):
    return render(request, 'Search_web.html')

def search_web(request):
    query = request.GET.get('q', '')
    search_type = request.GET.get('search_type', 'naver')
    results = []
    Count = 0
    
    if query:
        if search_type == 'naver':
            # 네이버 검색 결과를 크롤링
            url = f"https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={query}"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            # 검색 결과를 파싱
            for item in soup.select('.api_subject_bx'):
                lst_total_element = item.select_one('.lst_total')
                if lst_total_element is not None:
                    title_element = lst_total_element.select_one('.total_tit')
                    link_element = lst_total_element.select_one('[data-url]')
                    description_element = lst_total_element.select_one('.total_dsc')
                    
                    if title_element and link_element and description_element:
                        title = title_element.get_text()
                        link = link_element['data-url']
                        description = description_element.get_text()
                        results.append({'title': title, 'link': link, 'description': description})
        elif search_type == 'google':
            # 구글 검색 결과를 크롤링
            url = f"https://www.google.com/search?q={query}"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')

            # 검색 결과를 파싱 (예시로 뉴스 제목을 가져옴)
            for item in soup.select('.BVG0Nb'):
                title = item.get_text()
                link = item.find_parent('a')['href']
                results.append({'title': title, 'link': link})

    return render(request, 'Search_Web.html', {'q': query, 'results': results, 'search_type': search_type})


