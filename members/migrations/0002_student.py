# Generated by Django 4.1.6 on 2023-02-15 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('standard', models.IntegerField()),
                ('Rollno', models.IntegerField()),
                ('created_by', models.CharField(max_length=30)),
            ],
        ),
    ]
