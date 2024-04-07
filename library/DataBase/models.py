from django.db import models
from django.contrib.auth.models import User
from datetime import date

class User(models.Model):
    username_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    password = models.CharField(max_length=60)

    def __str__(self):
        return self.first_name

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True)
    answer = models.ForeignKey(Answers, on_delete=models.CASCADE, null=True, blank=True)

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
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.topic

    def clean(self):
        if self.tags.count() > 5:
            raise ValidationError("Максимальное число тегов 5")

class Answers(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=800)
    likes = models.IntegerField()


    
