from django.shortcuts import render
from .models import Question

# Create your views here.

def new_questions(request):
    new_questions = Question.objects.order_by('-created_at')[:5]
    return render(request, 'new_questions.html', {'new_questions': new_questions})

def popular_questions(request):
    popular_questions = Question.objects.annotate(num_likes=models.Count('like')).order_by('-num_likes')[:5]
    return render(request, 'popular_questions.html', {'popular_questions': popular_questions})

def questions_by_tag(request, tag_name):
    questions_by_tag = Question.objects.filter(tags__name=tag_name)
    return render(request, 'questions_by_tag.html', {'questions_by_tag': questions_by_tag})