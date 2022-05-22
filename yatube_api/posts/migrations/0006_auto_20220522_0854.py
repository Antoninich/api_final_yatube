# Generated by Django 2.2.16 on 2022-05-22 08:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20220522_0225'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='Вы уже подписаны на этого автора.',
        ),
        migrations.RemoveConstraint(
            model_name='follow',
            name='Нельзя подписываться на себя.',
        ),
        migrations.RenameField(
            model_name='follow',
            old_name='following',
            new_name='author',
        ),
        migrations.AlterField(
            model_name='follow',
            name='user',
            field=models.ForeignKey(help_text='Пользователь, который подписывается', on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь, который подписывается'),
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'author'), name='Вы уже подписаны на этого автора.'),
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.CheckConstraint(check=models.Q(_negated=True, user=django.db.models.expressions.F('author')), name='Нельзя подписываться на себя.'),
        ),
    ]