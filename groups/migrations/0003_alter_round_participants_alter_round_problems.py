# Generated by Django 4.2.5 on 2023-09-10 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_baekjoon_id'),
        ('problems', '0002_problem_problemsubmission_delete_group'),
        ('groups', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='round',
            name='participants',
            field=models.ManyToManyField(null=True, related_name='participated_rounds', to='users.user'),
        ),
        migrations.AlterField(
            model_name='round',
            name='problems',
            field=models.ManyToManyField(null=True, to='problems.problem'),
        ),
    ]