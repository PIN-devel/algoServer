# Generated by Django 4.2.5 on 2023-09-09 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('problems', '0002_problem_problemsubmission_delete_group'),
        ('groups', '0001_initial'),
        ('users', '0002_alter_user_baekjoon_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='round',
            name='problems',
            field=models.ManyToManyField(to='problems.problem'),
        ),
        migrations.AddField(
            model_name='group',
            name='leader',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='leading_groups', to='users.user'),
        ),
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(related_name='joined_groups', to='users.user'),
        ),
    ]
