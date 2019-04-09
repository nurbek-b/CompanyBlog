# Generated by Django 2.2 on 2019-04-09 05:53

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0012_auto_20190409_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 9, 5, 53, 2, 86304, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 9, 5, 53, 2, 87464, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='company',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 9, 5, 53, 2, 85065, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='CommentFavorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='is_favorite', to='blog.Comment')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Favorite Comment',
                'verbose_name_plural': 'Favorite Comments',
            },
        ),
    ]