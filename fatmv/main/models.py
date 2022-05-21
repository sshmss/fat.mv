from statistics import mode
from xmlrpc.client import DateTime
from django.contrib.postgres.fields import ArrayField
from django.db import models


class UserProfile(models.Model):
    role = models.CharField(max_length=50)
    name = models.CharField(max_length=200)

class Trainer(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.PROTECT)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=7)
    status = models.CharField(max_length=100)
    pic = models.FileField()
    certifications = models.FileField()

class Member(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.PROTECT)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=7)

class Application(models.Model):
    member = models.ForeignKey(UserProfile, on_delete=models.PROTECT, related_name='member_application')
    trainer = models.ForeignKey(UserProfile, on_delete=models.PROTECT, related_name='trainer_application')

class TrainerSchedule(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.PROTECT)
    start = models.DateTimeField()
    end = models.DateTimeField()
    status = models.CharField(max_length=100)

class Gym(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=500)

class GymTrainer(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.PROTECT)
    gym = models.ForeignKey(Gym, on_delete=models.PROTECT)
    pic = models.FileField()

class UserPreference(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.PROTECT)
    pref_key = models.CharField(max_length=500)
    pref_value = ArrayField(models.CharField(max_length=500))
