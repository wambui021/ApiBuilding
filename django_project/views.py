import requests
from django.shortcuts import render 
import random

def fact_page(request):
    response = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
    data = response.json()
    fact = data['text']
    return render(request, 'fact_page.html', {'fact': fact})

def student_page(request):
    response2 = requests.get('https://freetestapi.com/api/v1/students')
    data2 = response2.json()
    random_student = random.choice(data2)['name']
    return render(request, 'student_page.html', {'name': random_student})

def image_page(request):
    r3 = requests.get('https://dog.ceo/api/breeds/image/random')
    res3 = r3.json()
    dog = res3['message']
    return render(request, 'image_page.html', {'dog': dog})

  