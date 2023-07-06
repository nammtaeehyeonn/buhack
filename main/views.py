from django.shortcuts import render
import requests
import json
import pandas as pd

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