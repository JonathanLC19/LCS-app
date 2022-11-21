from django.db import models



class Stage(models.Model):
    stage_name = models.CharField(max_length=75)

    def __str__(self):
         return self.stage_name

class Definition(models.Model):
    pass

class Tools(models.Model):
    pass

class Trigger(models.Model):
    pass

class OwnerTeam(models.Model):
    pass