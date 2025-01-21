from django.db import models

class Creator(models.Model):
    name = models.CharField(max_length=100, unique=True)
    money = models.FloatField(default=0)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Member(models.Model):
    name = models.CharField(max_length=100)
    endurance = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class TeamApplication(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.member.name} -> {self.team.name}"
