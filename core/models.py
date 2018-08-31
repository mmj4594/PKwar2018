from django.db import models

class LiveMatch(models.Model):
    match_name = models.CharField(max_length=20, default="sports")
    경기명 = models.CharField(max_length=20, default="경기")
    p_score = models.IntegerField(default=0)
    k_score = models.IntegerField(default = 0)
    which_video = models.TextField(blank=True)
    which_chat = models.TextField(default="", blank=True)
    def __str__(self):
        return self.match_name

class FinishedMatch(models.Model):
    match_name = models.CharField(max_length=20, default="sports")
    p_score = models.IntegerField(default=0)
    k_score = models.IntegerField(default=0)
    게임명 = models.CharField(max_length=20, default="경기")
    which_video = models.TextField(blank=True)
    def __str__(self):
        return self.match_name

class Result(models.Model):
    p_score = models.IntegerField(default=0)
    k_score = models.IntegerField(default=0)
    is_end = models.BooleanField(default=False)
    is_live = models.BooleanField(default=False)