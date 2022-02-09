from django.core.validators import (MaxValueValidator,
                                    MinValueValidator, ValidationError)
from django.db import models
from django.utils import timezone

from users.models import User


class Genre(models.Model):

    name = models.CharField(
        max_length=200,
        verbose_name='Название жанра',
        help_text='Укажите название жанра',
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name='Адрес',
        help_text=('Укажите адрес для страницы жанра. Используйте только '
                     'латиницу, цифры, дефисы и знаки подчёркивания'),
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'genre'
        verbose_name_plural = 'genres'

    def __str__(self):
        return self.name


class Category(models.Model):

    name = models.CharField(
        max_length=256,
        verbose_name='Название категории',
        help_text='Укажите название категории',
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name='Адрес',
        help_text=('Укажите адрес для страницы категории. Используйте только '
                   'латиницу, цифры, дефисы и знаки подчёркивания'),
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


def year_validator(value):
    if value > timezone.now().year:
        raise ValidationError('Год не может быть больше текущего')


class Title(models.Model):

    name = models.CharField(
        max_length=256,
        verbose_name='Название произведения',
        help_text='Укажите название произведения',
        db_index=True
    )
    year = models.IntegerField(
        verbose_name='Год выхода произведения',
        help_text='Укажите год выхода произведения',
        validators=[
            year_validator
        ]
    )

    description = models.CharField(
        max_length=200,
        verbose_name='Описание произведения',
        help_text='Укажите описание произведения',
    )

    genre = models.ManyToManyField(
        Genre,
        through='GenreTitle',
        verbose_name='Жанр',
        help_text='Укажите жанр',
        db_index=True
    )

    category = models.ForeignKey(
        Category,
        related_name='titles',
        on_delete=models.CASCADE,
        verbose_name='Категория',
        help_text='Укажите категорию',
        db_index=True
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'title'
        verbose_name_plural = 'titles'

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    title = models.ForeignKey(
        Title,
        null=True,
        on_delete=models.CASCADE,
        verbose_name='Произведения',
        related_name='genre_titles',
        db_index=True
    )
    genre = models.ForeignKey(
        Genre,
        null=True,
        on_delete=models.CASCADE,
        verbose_name='жанр',
        related_name='genre_titles',
        db_index=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'genre'],
                name="unique_genre_title")
        ]

        ordering = ['title']
        verbose_name = 'genre_title'
        verbose_name_plural = 'genre_titles'


class Review(models.Model):
    title = models.ForeignKey(
        Title, verbose_name='Название произведения',
        on_delete=models.CASCADE, related_name='reviews', db_index=True)
    author = models.ForeignKey(
        User, verbose_name='Автор обзора',
        on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField(verbose_name='Текст обзора')
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации', auto_now_add=True, db_index=True)
    score = models.IntegerField(
        verbose_name='Оценка',
        validators=[
            MinValueValidator(1, message='Минимальное значение: 1'),
            MaxValueValidator(10, message='Максимальное значение: 10')
        ]
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'],
                name='unique_reviewing')
        ]
        ordering = ['pub_date']
        verbose_name = 'review'
        verbose_name_plural = 'reviews'


class Comment(models.Model):
    review = models.ForeignKey(
        Review, verbose_name='Комментируемый обзор',
        on_delete=models.CASCADE, related_name='comments', db_index=True)
    text = models.TextField(verbose_name='Текст комментария')
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации', auto_now_add=True, db_index=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор комментария'
    )

    class Meta:
        ordering = ['pub_date']
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
