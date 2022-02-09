from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueTogetherValidator
from reviews.models import Category, Comment, Genre, Review, Title

User = get_user_model()


class ReviewSerializer(serializers.ModelSerializer):
    title = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True,
    )
    author = serializers.SlugRelatedField(
        default=serializers.CurrentUserDefault(),
        slug_field='username',
        read_only=True,
    )

    def validate(self, data):
        request = self.context['request']
        if request.method != 'POST':
            return data
        title_id = self.context['view'].kwargs.get('title_id')
        title = get_object_or_404(Title, id=title_id)
        if title.reviews.filter(author=request.user).exists():
            raise ValidationError('You are allowed to leave only one'
                                  ' review')
        return data

    class Meta:
        model = Review
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    review = serializers.SlugRelatedField(
        slug_field='text',
        read_only=True
    )
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        fields = '__all__'
        model = Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['id']
        model = Category
        extra_kwargs = {'lookup_field': 'slug'}
        validators = [
            UniqueTogetherValidator(
                queryset=Category.objects.all(),
                fields=('name', 'slug'),
                message='Такая категория уже существует'
            )
        ]


class GenreSerializer(serializers.ModelSerializer):
    extra_kwargs = {'lookup_field': 'slug'}

    class Meta:
        exclude = ['id']
        model = Genre

        validators = [
            UniqueTogetherValidator(
                queryset=Genre.objects.all(),
                fields=('name', 'slug'),
                message='Такой жанр уже существует'
            )
        ]


class TitleListSerializer(serializers.ModelSerializer):

    genre = GenreSerializer(many=True, required=True)
    category = CategorySerializer(required=True)
    rating = serializers.FloatField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Title


class TitleSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        many=True,
        slug_field='slug',
        queryset=Genre.objects.all()
    )
    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Category.objects.all()
    )

    class Meta:
        fields = ('id', 'name', 'year',
                  'description', 'genre', 'category',)
        model = Title

    def validate(self, data):
        if data.get('year') and data['year'] > timezone.now().year:
            raise serializers.ValidationError(
                'год выпуска не может быть больше текущего')
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('email', 'role', 'first_name',
                  'last_name', 'username', 'bio')
        model = User


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('email', 'username')
        model = User


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    confirmation_code = serializers.CharField()
