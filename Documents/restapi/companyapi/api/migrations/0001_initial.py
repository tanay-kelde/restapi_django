# Generated by Django 4.2.2 on 2023-06-30 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('comapny_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('about', models.TextField()),
                ('type', models.CharField(choices=[('IT', 'IT'), ('non IT', 'non IT'), ('phone', 'phone')], max_length=100)),
                ('added_date', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
