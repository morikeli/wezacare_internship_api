from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Questions, Answers
import uuid


@receiver(pre_save, sender=Questions)
def generate_questionID(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace('-', '').upper()[:10]


@receiver(pre_save, sender=Answers)
def generate_answersID(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace('-', '').upper()[:10]

