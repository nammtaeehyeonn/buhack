from django.shortcuts import render
import requests
import json
import pandas as pd
from django.http import JsonResponse

# CSV 파일 경로
file_path = '/mnt/c/Users/pc/PycharmProjects/pythonProject7/mysite/main/busan.csv'

# CSV 파일을 데이터프레임으로 변환
busan_df = pd.read_csv(file_path, encoding='cp949')
# busan_df_data = busan_df[['제목', '위도', '경도']]

def df(request):
    busan_df_data = busan_df[['제목', '위도', '경도', '내용']]
    markers = []
    for _, row in busan_df_data.iterrows():
        title = row['제목']
        lat = row['위도']
        lng = row['경도']
        con = row['내용']
        marker = {
            'title': title,
            'lat': lat,
            'lng': lng,
            'con': con
        }
        markers.append(marker)

    context = {
        'markers': markers
    }
    return render(request, 'main_page.html', context)

# Create your views here.
def index(request):
    return render(request, 'index.html')

def index222(request):
    busan_df_data = busan_df[['제목', '위도', '경도', '내용', '이미지주소','맛집1','맛집2','맛집3','숙소1','숙소2','숙소3', '부제']]
    markers = []
    for _, row in busan_df_data.iterrows():
        title = row['제목']
        lat = row['위도']
        lng = row['경도']
        con = row['부제']         # 이거 요약본임
        image_url = row['이미지주소']
        food1 = row['맛집1']
        food2 = row['맛집2']
        food3 = row['맛집3']
        home1 = row['숙소1']
        home2 = row['숙소2']
        home3 = row['숙소3']
        allcon = row['내용']     # 이거 원본임

        marker = {
            'title': title,
            'lat': lat,
            'lng': lng,
            'con': con,
            'image_url': image_url,
            'food1': food1,
            'food2': food2,
            'food3': food3,
            'home1': home1,
            'home2': home2,
            'home3': home3,
            'allcon': allcon,
        }
        markers.append(marker)

    context = {
        'markers': markers
    }
    return render(request, 'index222.html', context)

def aaa(request):
    return render(request, 'aaa.html')

def bbb(request):
    return render(request, 'bbb.html')

def ccc(request):
    return render(request, 'ccc.html')

def map(request):
    return render(request, 'map.html')

def detail(request):
    return render(request, 'detail.html')