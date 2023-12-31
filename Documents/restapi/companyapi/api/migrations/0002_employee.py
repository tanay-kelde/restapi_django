# Generated by Django 4.2.2 on 2023-07-01 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('adress', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=10)),
                ('about', models.TextField()),
                ('position', models.CharField(choices=[('manager', 'mg'), ('softwere developer', 'sd'), ('project', 'pj')], max_length=100)),
                ('Company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Employee', to='api.company')),
            ],
        ),
    ]
