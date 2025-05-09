# Generated by Django 5.0.2 on 2024-04-21 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0007_link_reviews'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Имя ссылки', max_length=100)),
                ('review', models.TextField(default='Ваш отзыв')),
            ],
        ),
        migrations.AlterField(
            model_name='link',
            name='reviews',
            field=models.JSONField(default=list),
        ),
    ]
