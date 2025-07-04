# Generated by Django 5.2 on 2025-06-01 22:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chapters', '0002_initial'),
        ('contacts', '0001_initial'),
        ('partners', '0001_initial'),
        ('regions', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='contactnote',
            name='created_by',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name='contact_notes',
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name='historicalcontact',
            name='chapter',
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name='+',
                to='chapters.chapter',
            ),
        ),
        migrations.AddField(
            model_name='historicalcontact',
            name='history_user',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='+',
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name='historicalcontact',
            name='partner_campaign',
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name='+',
                to='partners.partnercampaign',
            ),
        ),
        migrations.AddField(
            model_name='historicalcontact',
            name='zip_code',
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name='+',
                to='regions.zip',
            ),
        ),
        migrations.AddField(
            model_name='contactnote',
            name='contact',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='notes',
                to='contacts.contact',
            ),
        ),
        migrations.AddField(
            model_name='contact',
            name='chapter',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name='%(class)ss',
                to='chapters.chapter',
            ),
        ),
        migrations.AddField(
            model_name='contact',
            name='partner_campaign',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='%(class)ss',
                to='partners.partnercampaign',
            ),
        ),
        migrations.AddField(
            model_name='contact',
            name='zip_code',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name='%(class)ss',
                to='regions.zip',
            ),
        ),
        migrations.AddField(
            model_name='expungedcontact',
            name='chapter',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name='expunged_contacts',
                to='chapters.chapter',
            ),
        ),
        migrations.AddField(
            model_name='expungedcontact',
            name='partner_campaign',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to='partners.partnercampaign',
            ),
        ),
        migrations.AddField(
            model_name='pendingcontact',
            name='chapter',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name='%(class)ss',
                to='chapters.chapter',
            ),
        ),
        migrations.AddField(
            model_name='pendingcontact',
            name='partner_campaign',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='%(class)ss',
                to='partners.partnercampaign',
            ),
        ),
        migrations.AddField(
            model_name='pendingcontact',
            name='zip_code',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name='%(class)ss',
                to='regions.zip',
            ),
        ),
        migrations.AddField(
            model_name='removedcontact',
            name='removed_by',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
