# Generated by Django 4.2 on 2023-08-13 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0008_alter_doctoranswer_board_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctoranswer',
            name='answer',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]