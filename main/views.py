import pandas as pd
from pymongo import MongoClient
from .models import Image

from django.shortcuts import render, redirect
from .forms import ImageForm
import openai

# CSV 파일 경로
file_path = '/mnt/c/Users/pc/PycharmProjects/pythonProject7/mysite/main/busan.csv'

# CSV 파일을 데이터프레임으로 변환
busan_df = pd.read_csv(file_path, encoding='utf8')
busan_df_data = busan_df[['제목', '위도', '경도', '내용', '이미지주소', '맛집1', '맛집2', '맛집3', '숙소1', '숙소2', '숙소3', '부제', '내용요약']]
markers = []
for _, row in busan_df_data.iterrows():
    title = row['제목']
    lat = row['위도']
    lng = row['경도']
    con = row['부제']  # 이거 요약본임
    image_url = row['이미지주소']
    food1 = row['맛집1']
    food2 = row['맛집2']
    food3 = row['맛집3']
    home1 = row['숙소1']
    home2 = row['숙소2']
    home3 = row['숙소3']
    allcon = row['내용']  # 이거 원본임

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

client = MongoClient("mongodb://localhost:27017")
db = client['busan_hack']  # DB명
collection = db['main_image']  # 컬렉션 명

def question_chat(request):
    images = collection.find()

    if request.method == 'POST':
        question = request.POST.get('question', '')

        openai.api_key = '***'

        messages = []

        content = question + ',3줄내로 내용을 요약해서 작성해줘'
        messages.append({"role": "user", "content": content})
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        chat_response = completion.choices[0].message.content

        context = {
            'markers': markers,
            'images': images,
            'chat_response': chat_response
        }

        return render(request, 'index222.html', context)

    return render(request, 'index222.html')


# Create your views here.

def index222(request):
    images = collection.find()
    context = {
        'markers': markers,
        'images': images
    }
    return render(request, 'index222.html', context)


def upupup(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            # 폼에서 이미지와 이름을 가져옴
            image = form.cleaned_data['image']
            name = form.cleaned_data['name']

            # 데이터를 몽고DB에 적재
            busan_hack_DB=Image(image=image, name=name)
            busan_hack_DB.save()
            # data = {'image': image, 'name': name}

            # collection.insert_one(data)

            return redirect('main:index222')
    else:
        form = ImageForm()

    return render(request, 'index222.html', {'form': form})