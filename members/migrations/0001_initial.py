# Generated by Django 4.1.6 on 2023-02-15 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=225)),
                ('lastname', models.CharField(max_length=225)),
                ('mobile_no', models.IntegerField()),
                ('joined_date', models.DateField(null=True)),
            ],
        ),
    ]
