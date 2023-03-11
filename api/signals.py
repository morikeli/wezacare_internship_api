from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Questions, Answers, User
import uuid


@receiver(pre_save, sender=User)
def generate_userID(sender, instance, **kwargs):
    """
        By default django assigns users with IDs base on AutoField.
        This function overides this system by generating IDs using uuid numbers
        with a 10 characters.
    """
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace('-', '').upper()[:10]



@receiver(pre_save, sender=Questions)
def generate_questionID(sender, instance, **kwargs):
    """
        Generate IDs using uuid numbers by manipulating uuid module. Each question has unique IDs.
    """
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace('-', '').upper()[:10]


@receiver(pre_save, sender=Answers)
def generate_answersID(sender, instance, **kwargs):
    """
        Generate IDs using uuid numbers by manipulating uuid module. Each answer has unique IDs.
    """
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace('-', '').upper()[:10]

