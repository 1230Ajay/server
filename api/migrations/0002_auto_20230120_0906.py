# Generated by Django 3.2 on 2023-01-20 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contents',
            name='type',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Cats',
        ),
    ]
