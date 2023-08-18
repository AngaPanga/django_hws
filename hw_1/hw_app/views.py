from django.shortcuts import render
from django.http import HttpResponse
from random import randint
import logging

logger = logging.getLogger(__name__)

def text(title, text):
    return f'<h1>Мой сайт</h1>' \
           f'<h2>{title}</h2>' \
           f'<p>{text}</p>'

def general(request):
    title = 'Главная страница сайта'
    body_text = 'Текст главной страницы сайта, с наполнением'
    logger.info(f'Page "general" is open')
    return HttpResponse(text(title, body_text))

def about(request):
    title = 'О себе'
    body_text = 'Студент онлайн платформы Geekbrains<br>' \
                'Группа - Программист разработчик языка Python'
    logger.info(f'Page "about" is open')
    return HttpResponse(text(title, body_text))
