# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('url', models.URLField()),
                ('twitter', models.URLField(blank=True)),
                ('github', models.URLField(blank=True)),
                ('facebook', models.URLField(blank=True)),
                ('photo', models.URLField(blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('is_open', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TicketCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='ticket',
            name='category',
            field=models.ForeignKey(related_name='tickets', to='member.TicketCategory'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='ticket_member',
            field=models.ForeignKey(related_name='tickets', to='member.Member'),
        ),
        migrations.AddField(
            model_name='answer',
            name='member',
            field=models.ForeignKey(related_name='answers', to='member.Member'),
        ),
        migrations.AddField(
            model_name='answer',
            name='ticket_id',
            field=models.ForeignKey(related_name='answers', to='member.Ticket'),
        ),
    ]
