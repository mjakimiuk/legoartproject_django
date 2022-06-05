# Generated by Django 4.0.4 on 2022-05-30 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lego', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Art_project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('pdf', models.FileField(upload_to='art/pdfs')),
            ],
        ),
        migrations.DeleteModel(
            name='File',
        ),
        migrations.DeleteModel(
            name='Upload',
        ),
    ]