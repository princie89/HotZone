# Generated by Django 3.1.2 on 2020-10-16 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HotZone', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='Case',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HotZone.case'),
        ),
    ]
