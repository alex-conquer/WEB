from django.core.management import BaseCommand
from django.contrib.auth.models import User
from database.models import Profile, Question, Answer, Tag, Like
import random
import string


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('ratio', type=int)

    def handle(self, *args, **options):
        ratio = options['ratio']

        users_count = ratio
        questions_count = ratio * 10
        answers_count = ratio * 100
        tags_count = ratio
        likes_count = ratio * 200

        self.create_users_and_profiles(users_count)
        self.create_tags(tags_count)
        self.create_questions(questions_count)
        self.create_answers(answers_count)
        self.create_likes(likes_count)

    def generate_random_string(self, length=10):
        return ''.join(random.choices(string.ascii_letters, k=length))

    def create_users_and_profiles(self, count):
        print('Creating users and profiles')
        for _ in range(count):
            username = self.generate_random_string()
            email = f'{username}@example.com'
            password = self.generate_random_string(8)
            user = User.objects.create(username=username, email=email)
            Profile.objects.create(user=user)
        print('Finish creating users and profiles')

    def create_tags(self, count):
        print('Creating tags')
        for _ in range(count):
            name = self.generate_random_string(8)
            Tag.objects.create(name=name)
        print('Finish creating tags')

    def create_questions(self, count):
        print('Creating questions')
        users = User.objects.all()
        tags = Tag.objects.all()
        for _ in range(count):
            title = self.generate_random_string(20)
            content = self.generate_random_string(100)
            author = random.choice(users)
            question = Question.objects.create(title=title, content=content, author=author)
            question.tags.set(random.sample(list(tags), k=random.randint(1, 3)))
        print('Finish creating questions')

    def create_answers(self, count):
        print('Creating answers')
        users = User.objects.all()
        questions = Question.objects.all()
        for _ in range(count):
            content = self.generate_random_string(100)
            question = random.choice(questions)
            author = random.choice(users)
            Answer.objects.create(question=question, content=content, author=author)
        print('Finish creating answers')

    def create_likes(self, count):
        print('Creating likes')
        users = User.objects.all()
        questions = Question.objects.all()
        answers = Answer.objects.all()
        for _ in range(count):
            user = random.choice(users)
            is_positive = random.choice([True, False])
            if random.choice([True, False]):
                question = random.choice(questions)
                if not Like.objects.filter(user=user, question=question).exists():
                    Like.objects.create(user=user, question=question, is_positive=is_positive)
            else:
                answer = random.choice(answers)
                if not Like.objects.filter(user=user, answer=answer).exists():
                    Like.objects.create(user=user, answer=answer, is_positive=is_positive)
        print('Finish creating likes')