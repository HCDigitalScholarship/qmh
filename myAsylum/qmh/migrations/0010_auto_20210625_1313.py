# Generated by Django 2.2.24 on 2021-06-25 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qmh', '0009_auto_20210625_1225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='admitAge',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='admitDateFull',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='admitMonth',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='admitYear',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='firstName',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='lastName',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='leaveDateFull',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='patientNumber',
        ),
    ]
