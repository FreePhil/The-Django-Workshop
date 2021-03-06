# Generated by Django 3.0a1 on 2020-02-05 04:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0006_auto_20200123_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(1, '☆'), (2, '☆☆'), (3, '☆☆☆'), (4, '☆☆☆☆'), (5, '☆☆☆☆☆')], help_text='The rating that the reviewer has given.'),
        ),
        migrations.CreateModel(
            name='ReviewerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='profile_photos/')),
                ('favourite_book', models.ForeignKey(help_text='Your favourite book (if it is present in Bookr)', null=True, on_delete=django.db.models.deletion.SET_NULL, to='reviews.Book')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
