# Generated by Django 4.0.4 on 2022-06-05 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lego', '0007_remove_artproject_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='artproject',
            name='title',
            field=models.CharField(default='defaultname', max_length=100),
            preserve_default=False,
        ),
    ]
