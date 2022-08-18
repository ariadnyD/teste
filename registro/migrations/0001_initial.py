# Generated by Django 4.1 on 2022-08-18 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('telefone', models.IntegerField()),
                ('nascimento', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('senha', models.CharField(max_length=50)),
                ('confirme_senha', models.CharField(max_length=50)),
            ],
        ),
    ]
