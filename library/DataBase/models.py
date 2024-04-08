from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Count

class TopQuestionsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().annotate(num_likes=Count('likes')).order_by('-num_likes')[:10]

class TaggedQuestionsManager(models.Manager):
    def get_queryset(self, tag_name):
        return super().get_queryset().filter(tags__name=tag_name)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, blank=True)

class Tag(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Question(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT)
    text = models.CharField(max_length=300)
    topic = models.CharField(max_length=120)
    likes = models.PositiveIntegerField(default=0)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(default=timezone.now)

    objects = models.Manager()
    top_question = TopQuestionsManager()
    tagged_questions = TaggedQuestionsManager()

class Answers(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT)
    # question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=800)
    likes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)

class Like(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
