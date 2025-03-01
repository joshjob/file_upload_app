# Generated by Django 5.0.6 on 2024-07-02 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0004_alter_originaldata_backlog_attempt_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='originaldata',
            name='course_category',
            field=models.CharField(choices=[('UG', 'Undergraduate'), ('PG', 'Postgraduate')], default='UG', max_length=2),
        ),
        migrations.AddField(
            model_name='originaldata',
            name='report_name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
