from django.db import models

class Creator(models.Model):
    name = models.CharField(max_length=100)
    points = models.FloatField(default=0)

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)

class Member(models.Model):
    name = models.CharField(max_length=100)
    endurance = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

class TeamApplication(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
