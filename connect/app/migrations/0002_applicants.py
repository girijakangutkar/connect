# Generated by Django 4.2 on 2023-08-03 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('ssc', models.IntegerField(null=True)),
                ('Hsc', models.IntegerField(null=True)),
                ('Postgrad_cgpa', models.IntegerField()),
                ('Resume', models.FileField(upload_to='')),
            ],
        ),
    ]
