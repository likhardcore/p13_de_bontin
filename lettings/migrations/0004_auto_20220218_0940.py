# Generated by Django 3.0 on 2022-02-18 09:40
from django.db import migrations
# from oc_lettings_site import models
from lettings.models import Address, Letting


def populate(apps, shema_editor):
    """
    Forgot to add "populate" in "operations".
    """
    lettings = Letting.objects.all()
    for letting in lettings:
        letting_address = Address.objects.get(id=letting.address.id)
        Letting(
            title=letting.title,
            address=letting_address
        ).save()

class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0003_auto_20220218_0936'),
    ]

    operations = [
        migrations.RunPython(populate)
    ]
