# Generated by Django 4.2.9 on 2024-01-11 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=220)),
                ('Email', models.EmailField(max_length=220)),
                ('Password', models.CharField(max_length=8)),
                ('Confirm_Password', models.CharField(max_length=8)),
            ],
        ),
    ]
