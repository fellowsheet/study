import datetime

from django.db import models
from accounts.models import User


# class Author(models.Model): #автор
#     name = models.CharField(
#         max_length=300, verbose_name='Имя автора',
#         help_text='Введите имя автора'
#     )
#     birth_date: datetime.date = models.DateField()
#
#     def get_age(self) -> int:
#         return (datetime.date.today() - self.birth_date).days // 365
#
#     def set_age(self, age: int):
#         self.birth_date = (
#                 datetime.date.today() - datetime.timedelta(days=365 * age))
#
#     age = property(get_age, set_age)
#
#     def __str__(self):
#         return f'{self.name} ({self.age})'

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


class Channel(models.Model):
    name_channel = models.CharField(max_length=100,
                                    verbose_name='Название канала')
    photo = models.ImageField(upload_to='photo/channel/%Y/%m/%d/',
                              verbose_name='Фото')
    bio = models.TextField(max_length=550,
                           verbose_name='Описание')
    admin = models.ForeignKey(User, on_delete=models.CASCADE,
                              verbose_name='Админ канала')
    slug = models.SlugField(max_length=50, unique=True, db_index=True,
                            verbose_name='URL')
    created = models.DateField(auto_now_add=True,
                               verbose_name='Время создания')

    def __str__(self):
        return self.name_channel

    class Meta:
        verbose_name = 'Канал'
        verbose_name_plural = 'Каналы'
        ordering = ['name_channel']


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=300, unique=True, db_index=True,
                            verbose_name='URL')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name='Автор')
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE,
                                verbose_name='Канал')
    content = models.TextField(blank=True, verbose_name='Текст поста')
    photo = models.ImageField(upload_to='photo/post/%Y/%m/%d/',
                              verbose_name='Фото')
    published = models.DateTimeField(auto_now_add=True,
                                     verbose_name='Время публикации')
    updated = models.DateTimeField(auto_now=True,
                                   verbose_name='Время изменения')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 verbose_name='Категория')
    likes = models.ManyToManyField(User, related_name='liked_posts',
                                   verbose_name='Количество лайков')
    views = models.PositiveIntegerField(default=0,
                                        verbose_name='Количество просмотров')

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ['-published', 'title']

    def __str__(self):
        return f'{self.title}, {self.author}'


class Comment(models.Model):
    commentator = models.ForeignKey(User, on_delete=models.CASCADE)
    published = models.DateTimeField(auto_now_add=True,
                                     verbose_name='Время публикации')
    text_comment = models.TextField(max_length=550,
                                    verbose_name='Текст комментария')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.commentator}, {self.post}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-published']


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.post}, {self.author}'

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'


class Follower(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE,
                                verbose_name='Канал')
    follower = models.ForeignKey(User, on_delete=models.CASCADE,
                                 verbose_name='Подписчик')

    def __str__(self):
        return f'{self.channel}, {self.follower}'

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'
