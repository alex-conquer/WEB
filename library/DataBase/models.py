from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone

# class TopQuestionsManager(models.Manager):
#     def get_queryset(self):
#         # Возвращаем вопросы, отсортированные по числу лайков в убывающем порядке
#         return super().get_queryset().annotate(num_likes=Count('likes')).order_by('-num_likes')[:10]

# class TaggedQuestionsManager(models.Manager):
#     def get_queryset(self, tag_name):
#         # Возвращаем вопросы, отмеченные заданным тегом
#         return super().get_queryset().filter(tags__name=tag_name)

class User(models.Model):
    username_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    password = models.CharField(max_length=60)

    def __str__(self):
        return self.first_name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    avatar = models.ImageField(null=True, blank=True)

class Tag(models.Model):
    name = models.CharField(max_length=50)

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    question_id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=300)
    topic = models.CharField(max_length=120)
    likes = models.IntegerField()
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(default=timezone.now)

    # top_question = TopQuestionsManager()
    # tagged_questions = TaggedQuestionsManager()

class Answers(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=800)
    likes = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True)
    answer = models.ForeignKey(Answers, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.topic

    # def clean(self):
    #     if self.tags.count() > 5:
    #         raise ValidationError({"tags": "Максимальное число тегов 5"})


    
