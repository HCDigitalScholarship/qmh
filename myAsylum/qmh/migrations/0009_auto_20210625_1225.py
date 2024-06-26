# Generated by Django 2.2.24 on 2021-06-25 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qmh', '0008_auto_20190722_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='age',
            field=models.IntegerField(blank=True, null=True, verbose_name='Present Age.'),
        ),
        migrations.AddField(
            model_name='patient',
            name='ageAtFirstAttack',
            field=models.IntegerField(blank=True, null=True, verbose_name='Age at First Attack.'),
        ),
        migrations.AddField(
            model_name='patient',
            name='bodilyCondition',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Bodily Condition: Good. Impaired. Bad.'),
        ),
        migrations.AddField(
            model_name='patient',
            name='causeOfInsanity',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Supposed Cause of Insanity.'),
        ),
        migrations.AddField(
            model_name='patient',
            name='civilConditionChildren',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Civil Condition: No. Children Living.'),
        ),
        migrations.AddField(
            model_name='patient',
            name='civilConditionMarriage',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Civil Condition: Married. Single. Widowed.'),
        ),
        migrations.AddField(
            model_name='patient',
            name='civilConditionSiblings',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Civil Condition: Bros. & Sisters Living.'),
        ),
        migrations.AddField(
            model_name='patient',
            name='complications',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Complications: Suicidal. Homicidal. Paralytic. Epileptic.. '),
        ),
        migrations.AddField(
            model_name='patient',
            name='congenitalIdiots',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Congenital Idiots.'),
        ),
        migrations.AddField(
            model_name='patient',
            name='dateOfAdmission',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Date of Admission'),
        ),
        migrations.AddField(
            model_name='patient',
            name='dateOfDischargeOrDeath',
            field=models.IntegerField(blank=True, null=True, verbose_name='Date of Discharge or Death.'),
        ),
        migrations.AddField(
            model_name='patient',
            name='dateOfLastAdmission',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Date of Last Previous Admission, if any.'),
        ),
        migrations.AddField(
            model_name='patient',
            name='dateOfMedicalCertificates',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Date of Medical Certificates, and by whom Signed.'),
        ),
        migrations.AddField(
            model_name='patient',
            name='durationOfExistingAttack',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Duration of Existing Attack: Years. Months. Days.'),
        ),
        migrations.AddField(
            model_name='patient',
            name='fullName',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Christian and Surname at Length.'),
        ),
        migrations.AddField(
            model_name='patient',
            name='mentalDisorder',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Form of Mental Disorder.'),
        ),
        migrations.AddField(
            model_name='patient',
            name='nameOfBodilyDisorder',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Name of Disorder, (Bodily), if any.'),
        ),
        migrations.AddField(
            model_name='patient',
            name='nativity',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Nativity.'),
        ),
        migrations.AddField(
            model_name='patient',
            name='numPreviousAttacks',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of Previous Attacks.'),
        ),
        migrations.AddField(
            model_name='patient',
            name='numberInOrderOfAdmission',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number in Order of Admission'),
        ),
        migrations.AddField(
            model_name='patient',
            name='occupation',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Occupation Prior to Insanity.'),
        ),
        migrations.AddField(
            model_name='patient',
            name='outcome',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name="Discharged: Restored. Improved. Much Impr'd. Stationary. Died."),
        ),
        migrations.AddField(
            model_name='patient',
            name='placeOfAbode',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Previous Place of Abode.'),
        ),
        migrations.AddField(
            model_name='patient',
            name='race',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Color.'),
        ),
        migrations.AddField(
            model_name='patient',
            name='relationsInsane',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Relations Insane.'),
        ),
        migrations.AddField(
            model_name='patient',
            name='remarks',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Remarks.'),
        ),
        migrations.AddField(
            model_name='patient',
            name='sex',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Sex'),
        ),
    ]
