# Generated by Django 4.2.4 on 2023-08-11 16:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '__first__'),
        ('doctor', '0006_alter_doctor_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='answer',
        ),
        migrations.AlterField(
            model_name='doctor',
            name='doctor_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='DoctorAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(blank=True, max_length=300, null=True)),
                ('board_list', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='board.board')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to='doctor.doctor')),
            ],
        ),
    ]
