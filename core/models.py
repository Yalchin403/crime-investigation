from django.db import models


class Suspect(models.Model):
    name = models.CharField(max_length=55)
    related_suspects = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return self.name


class Arm(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name


class Crime(models.Model):
    place = models.CharField(max_length=55)
    time_stamp = models.DateTimeField(auto_now_add=True)
    arms = models.ManyToManyField(Arm, blank=True)
    suspects = models.ManyToManyField(Suspect, blank=True)
    related_crimes = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return f"In {self.place} at {self.time_stamp}"