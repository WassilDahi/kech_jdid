# Generated by Django 3.2.4 on 2021-06-30 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_publication_date_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='date_published',
            field=models.DateTimeField(null=True),
        ),
    ]