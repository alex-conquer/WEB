from django.db import models
from django.contrib.auth.models import User

class PopularProfilesManager(models.Manager):
    def get_popular_profiles(self, count=5):
        queryset = self.get_queryset()
        return queryset.order_by('-rating')[:count]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='static/img/img.png', upload_to='avatars/', blank=True, null=True)
    rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = PopularProfilesManager()

    def str(self):
        return self.user.username


class PopularTagsManager(models.Manager):
    def get_popular_tags(self, count=5):
        return self.annotate(total_rating=models.Sum('question__rating')).order_by('-total_rating')[:count]


class Tag(models.Model):
    name = models.CharField(max_length=255)
    objects = PopularTagsManager()

    def str(self):
        return self.name


class QuestionQuerySet(models.QuerySet):
    def order_by_creation(self):
        queryset = self.get_queryset()
        return queryset.order_by('-created_at')

    def order_by_popularity(self):
        queryset = self.get_queryset()
        return queryset.order_by('-rating')

    def filter_by_tag(self, tag_name):
        queryset = self.get_queryset()
        return queryset.filter(tagsnameexact=tag_name)

    def filter_by_author(self, author):
        queryset = self.get_queryset()
        return queryset.filter(authornameexact=author)


class Question(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag')
    rating = models.IntegerField(default=0)
    objects = QuestionQuerySet()


class AnswerManager(models.Manager):
    def toggle_correct_answer(self, user, question, answer):
        if user == question.author:
            value = not answer.is_correct
            Answer.objects.filter(pk=answer.id).update(is_correct=value)
        pass


class Answer(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    objects = AnswerManager()


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True, blank=True)
    is_positive = models.BooleanField(default=True)