# Generated by Django 3.1.2 on 2020-10-16 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcardionSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(blank=True, max_length=200)),
                ('title1_text', models.TextField(blank=True)),
                ('title2', models.CharField(blank=True, max_length=200)),
                ('title2_text', models.TextField(blank=True)),
                ('title3', models.CharField(blank=True, max_length=200)),
                ('title3_text', models.TextField(blank=True)),
                ('photo', models.ImageField(blank=True, upload_to='img_of_product')),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]
