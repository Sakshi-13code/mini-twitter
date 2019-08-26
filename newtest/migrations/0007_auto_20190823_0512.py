# Generated by Django 2.2.3 on 2019-08-23 05:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('newtest', '0006_auto_20190820_1125'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to=settings.AUTH_USER_MODEL)),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('following', 'follower')},
            },
        ),
        migrations.CreateModel(
            name='TweetLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='like',
            name='tweet',
        ),
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
        migrations.AlterModelOptions(
            name='tweet',
            options={'ordering': ['-created_on']},
        ),
        migrations.RenameField(
            model_name='tweet',
            old_name='date',
            new_name='created_on',
        ),
        migrations.AlterField(
            model_name='tweet',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tweets', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Follow',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
        migrations.AddField(
            model_name='tweetlike',
            name='tweet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tweetlikes', to='newtest.Tweet'),
        ),
        migrations.AddField(
            model_name='tweetlike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userlike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='tweetlike',
            unique_together={('tweet', 'user')},
        ),
    ]
