# Generated by Django 2.2.19 on 2022-09-30 22:55

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AmountOfIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Количество ингредиентов')),
            ],
            options={
                'verbose_name': 'Количество ингредиентов',
                'verbose_name_plural': 'Количество ингредиентов',
            },
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
            ],
            options={
                'verbose_name': 'Избранное',
                'verbose_name_plural': 'Избранное',
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Укажите название ингредиента', max_length=100, verbose_name='Название ингредиента')),
                ('measurement_unit', models.CharField(help_text='Укажите единицу измерения ингредиента', max_length=100, verbose_name='Единица измерения')),
            ],
            options={
                'verbose_name': 'Ингредиент',
                'verbose_name_plural': 'Ингредиенты',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Укажите название рецепта', max_length=100, verbose_name='Название рецепта')),
                ('image', models.ImageField(upload_to='media/', verbose_name='Изображение блюда')),
                ('text', models.TextField(help_text='Введите описание рецепта', verbose_name='Описание рецепта')),
                ('cooking_time', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1, 'Значение не может быть меньше 1')], verbose_name='Время готовки блюда в минутах')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Название тега')),
                ('slug', models.SlugField(help_text='Ссылка тега', unique=True, verbose_name='Ссылка')),
                ('color', models.CharField(default='#ffffff', max_length=7, unique=True, verbose_name='Цвет тэга')),
            ],
            options={
                'verbose_name': 'Тэг',
                'verbose_name_plural': 'Тэги',
            },
        ),
        migrations.CreateModel(
            name='ShoppingList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to='recipes.Recipe', verbose_name='Покупка')),
            ],
            options={
                'verbose_name': 'Список покупок',
                'verbose_name_plural': 'Список покупок',
            },
        ),
    ]
