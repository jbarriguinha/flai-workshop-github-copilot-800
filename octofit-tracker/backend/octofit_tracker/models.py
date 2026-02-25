from djongo import models


class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    class Meta:
        app_label = 'octofit_tracker'


class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, blank=True)

    class Meta:
        app_label = 'octofit_tracker'


class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField(help_text='Duration in minutes')
    date = models.DateField()

    class Meta:
        app_label = 'octofit_tracker'


class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()

    class Meta:
        app_label = 'octofit_tracker'


class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    exercises = models.JSONField(default=list)

    class Meta:
        app_label = 'octofit_tracker'
