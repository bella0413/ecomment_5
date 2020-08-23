import requests, json, cssutils
from bs4 import BeautifulSoup
from django.db import IntegrityError
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from news.models import SearchNews
from django.core.paginator import Paginator
import os
## Python이 실행될 때 DJANGO_SETTINGS_MODULE이라는 환경 변수에 현재 프로젝트의 settings.py파일 경로를 등록합니다.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Ecomment.settings")
## 이제 장고를 가져와 장고 프로젝트를 사용할 수 있도록 환경을 만듭니다.
import django
django.setup()


class GetIndexView(View):
    def get(self, request):
        return render(request, 'news/index.html')

class GetPolicyView(View):
    
    model = SearchNews
    context_object_name = 'SearchNews'
    paginate_by = 8

    def get(self, request):
        policy_url = 'http://www.chemicalnews.co.kr/news/articleList.html?sc_section_code=S1N1&view_type=sm'
        req = requests.get(policy_url)
        req.encoding = 'utf-8'
        html = req.text

        soup = BeautifulSoup(html, 'html.parser')
        list_items = soup.find_all('div', class_='list-block')

        policy_data = []
        chemical = 'http://www.chemicalnews.co.kr/'

        for item in list_items:
            
            title = item.find('div',class_='list-titles').text

            link = item.find('div',class_='list-image').find('a')
            if 'href' in link.attrs:
                conn = link.attrs['href']

            image= item.find('div',class_='list-image')['style']
            
            style = cssutils.parseStyle(image)
            url = style['background-image']
            url = url.replace('url(.','').replace(')','')

            content = item.find('p',class_='list-summary').text

            etc = item.find('div',class_='list-dated').text
            
            policy_data.append(
                {
                'title': title,
                'link': chemical + conn,
                'img': chemical + 'news/'+ url,
                'content': content[0:150],
                'etc': etc
                }
            )
        return render(request, 'news/policy.html',{'policy_data' : policy_data})
    #     return policy_data
        
    # policy_data = policy()
    # for item in policy_data:
    #     t = item.get('title')
    #     l = item.get('link')
    #     i = item.get('img')
    #     c = item.get('content')
    #     e = item.get('etc')
    #     SearchNews(title=t, link=l,img=i, content=c,etc=e).save()

    # for t,l,i,c,e in policy_data.items():
    #     SearchNews(title=t, link=l).save()
        # return render(request, 'news/policy.html',{'policy_data' : policy_data})
        # return JsonResponse({'policy_data' : policy_data}, status = 200, json_dumps_params={'ensure_ascii': False})  
        # 결과를 JsonResponse 규격에 맞는 dictionary형태로 return해준다.

class GetIssueView(View):
    def get(self, request):
        issue_url = 'http://www.chemicalnews.co.kr/news/articleList.html?sc_section_code=S1N3&view_type=sm'
        req = requests.get(issue_url)
        req.encoding = 'utf-8'
        html = req.text

        soup = BeautifulSoup(html, 'html.parser')
        list_items = soup.find_all('div', class_='list-block')

        issue_data = []
        chemical = 'http://www.chemicalnews.co.kr/'
        #chemical = 'http://www.newspenguin.com'

        for item in list_items:
            
            title = item.find('div',class_='list-titles').text

            link = item.find('div',class_='list-image').find('a')
            if 'href' in link.attrs:
                conn = link.attrs['href']

            image= item.find('div',class_='list-image')['style']
            
            style = cssutils.parseStyle(image)
            url = style['background-image']
            url = url.replace('url(.','').replace(')','')

            content = item.find('p',class_='list-summary').text

            etc = item.find('div',class_='list-dated').text
            
            issue_data.append(
                {
                'title': title,
                'link': chemical + conn,
                'img': chemical + 'news/'+ url,
                'content': content[0:150],
                'etc': etc
                }
            )
        return render(request, 'news/issue.html',{'issue_data' : issue_data})
        # return JsonResponse({'policy_data' : policy_data}, status = 200, json_dumps_params={'ensure_ascii': False})  
        # 결과를 JsonResponse 규격에 맞는 dictionary형태로 return해준다.

class GetEnterpriseView(View):
    def get(self, request):
        enter_url = 'http://www.newspenguin.com/news/articleList.html?sc_section_code=S1N5&view_type=sm'
        req = requests.get(enter_url)
        req.encoding = 'utf-8'
        html = req.text

        soup = BeautifulSoup(html, 'html.parser')
        list_items = soup.find_all('div', class_='list-block')

        enter_data = []
        chemical = 'http://www.newspenguin.com/'

        for item in list_items:
            
            title = item.find('div',class_='list-titles').text

            link = item.find('div',class_='list-image').find('a')
            if 'href' in link.attrs:
                conn = link.attrs['href']

            image= item.find('div',class_='list-image')['style']
            
            style = cssutils.parseStyle(image)
            url = style['background-image']
            url = url.replace('url(.','').replace(')','')

            content = item.find('p',class_='list-summary').text

            etc = item.find('div',class_='list-dated').text
            
            enter_data.append(
                {
                'title': title,
                'link': chemical + conn,
                'img': chemical + 'news/'+ url,
                'content': content[0:150],
                'etc': etc
                }
            )
        return render(request, 'news/enterprise.html',{'enter_data' : enter_data})
        # return JsonResponse({'policy_data' : policy_data}, status = 200, json_dumps_params={'ensure_ascii': False})  
        # 결과를 JsonResponse 규격에 맞는 dictionary형태로 return해준다.

class GetEtcView(View):
    def get(self, request):
        etc_url = 'http://www.newspenguin.com/news/articleList.html?sc_section_code=S1N9&view_type=sm'
        req = requests.get(etc_url)
        req.encoding = 'utf-8'
        html = req.text

        soup = BeautifulSoup(html, 'html.parser')
        list_items = soup.find_all('div', class_='list-block')

        etc_data = []
        #chemical = 'http://www.chemicalnews.co.kr/'
        chemical = 'http://www.newspenguin.com/'

        for item in list_items:
            
            title = item.find('div',class_='list-titles').text

            link = item.find('div',class_='list-image').find('a')
            if 'href' in link.attrs:
                conn = link.attrs['href']

            image= item.find('div',class_='list-image')['style']
            
            style = cssutils.parseStyle(image)
            url = style['background-image']
            url = url.replace('url(.','').replace(')','')

            content = item.find('p',class_='list-summary').text

            etc = item.find('div',class_='list-dated').text
            
            etc_data.append(
                {
                'title': title,
                'link': chemical + conn,
                'img': chemical + 'news/'+ url,
                'content': content[0:150],
                'etc': etc
                }
            )
        return render(request, 'news/etc.html',{'etc_data' : etc_data})
        # return JsonResponse({'policy_data' : policy_data}, status = 200, json_dumps_params={'ensure_ascii': False})  
        # 결과를 JsonResponse 규격에 맞는 dictionary형태로 return해준다.
