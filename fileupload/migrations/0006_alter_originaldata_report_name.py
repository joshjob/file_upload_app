# Generated by Django 5.0.6 on 2024-07-02 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0005_originaldata_course_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='originaldata',
            name='report_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
