# Generated by Django 3.1.1 on 2020-10-07 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_new_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50, verbose_name='тип блока')),
                ('text', models.CharField(max_length=300, verbose_name='текст блока')),
            ],
            options={
                'verbose_name': 'Блок сайта',
                'verbose_name_plural': 'Блоки сайта',
            },
        ),
        migrations.AlterField(
            model_name='document',
            name='description',
            field=models.CharField(blank=True, max_length=255, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='document',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки'),
        ),
        migrations.AlterField(
            model_name='document',
            name='url',
            field=models.SlugField(blank=True, null=True, unique=True, verbose_name='Путь'),
        ),
    ]