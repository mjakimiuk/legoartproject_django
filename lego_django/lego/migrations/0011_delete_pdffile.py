# Generated by Django 4.0.4 on 2022-06-05 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lego', '0010_remove_pdffile_img_pdffile_pdf'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PDFFile',
        ),
    ]
