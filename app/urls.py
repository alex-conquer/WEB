from django.urls import path

from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hot/', views.hot, name='hot'),
    path('questions/<int:question_id>', views.question, name='question'),
    path('ask/', views.ask, name='ask'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('settings/', views.settings, name='settings'),
    path('tag/', views.tag, name='tag'),
    path('tag/blablabla/', views.blablabla, name='blablabla'),
    path('answer/',views.answer, name = 'answer')
]



