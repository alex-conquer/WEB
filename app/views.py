from django.core.paginator import Paginator
from django.shortcuts import render

QUESTIONS = [
    {
        "id": i,
        "title": f"Question {i}",
        "text": f"This is question number {i}"
    } for i in range(200)
]

def index(request):
    # Получение номера страницы из запроса (если есть)
    page_num = request.GET.get('page', 1)
    
    
    page_num = int(page_num)
    

    # Преобразование строки в целое число
    page_num = int(page_num)

    if page_num < 1:
        page_num = 1
    elif page_num > 40:
        page_num = 30

    # Создание пагинатора и получение объекта страницы
    paginator = Paginator(QUESTIONS, 5)
    page_obj = paginator.page(page_num)
    
    # Возвращение шаблона с объектом страницы в контексте
    return render(request, "index.html", {"questions": page_obj})

# def index(request):
#     page_num = request.GET.get('page', 1)
#     paginator = Paginator(QUESTIONS, 5)
#     page_obj = paginator.page(page_num)
#     return render(request, "index.html", {"questions": page_obj})


def hot(request):
    page_num = request.GET.get('page', 1)
    paginator = Paginator(QUESTIONS[5:],5)
    page_obj = paginator.page(page_num)
    return render(request, "hot.html", context={"questions": page_obj})


def question(request, question_id):
    item = QUESTIONS[question_id]
    return render(request, template_name="question_detail.html", context={"question": item})

def ask(request):
    return render(request, "ask.html")

def login(request):
    return render(request, "login.html")

def signup(request):
    return render(request, "signup.html")

def settings(request):
    return render(request, "settings.html")

def tag(request):
    page_num = request.GET.get('page', 1)
    paginator = Paginator(QUESTIONS[5:],5)
    page_obj = paginator.page(page_num)
    return render(request, template_name="TegsListQuestion.html", context={"question":page_obj})

def blablabla(request):
    page_num = request.GET.get('page', 1)
    paginator = Paginator(QUESTIONS[5:],5)
    page_obj = paginator.page(page_num)
    return render(request, template_name="blablabla.html", context={"question":page_obj})