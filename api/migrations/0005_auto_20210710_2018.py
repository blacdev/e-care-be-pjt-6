# Generated by Django 3.2.4 on 2021-07-10 20:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0004_patient_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthofficer',
            name='city',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='healthofficer',
            name='lga',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='healthofficer',
            name='state',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='healthofficer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='health_officer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='health_officers',
            field=models.ManyToManyField(related_name='hospitals', to='api.HealthOfficer'),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='patients',
            field=models.ManyToManyField(related_name='hospitals', to='api.Patient'),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='hospital', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='hospital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='api.hospital'),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='api.patient'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='patient', to=settings.AUTH_USER_MODEL),
        ),
    ]
