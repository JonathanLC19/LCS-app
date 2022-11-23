from django.db import models



class Stage(models.Model):

    class StageChoices(models.IntegerChoices):
        subscriber = 1
        lead = 2
        mql = 3
        sql = 4
        opportunity = 5
        customer = 6

    class TeamChoices(models.IntegerChoices):
        marketing = 1
        sales = 2
        customer_care = 3

    stage_name = models.PositiveSmallIntegerField(choices= StageChoices.choices)
    stage_description = models.CharField(max_length= 500, default= '')
    stage_tools = models.CharField(max_length= 500, default= '')
    stage_trigger = models.CharField(max_length= 500, default= '')
    owner_team= models.PositiveSmallIntegerField(choices= TeamChoices.choices, default = 1)

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