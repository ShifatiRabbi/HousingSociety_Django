from django.db import models
from django.contrib.auth.models import User

class CommunityCenter(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    capacity = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name
    

class PlayGround(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    capacity = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    community_center = models.ForeignKey(CommunityCenter, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"{self.member} - {self.community_center} - {self.date}"
    

class BookingGround(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    play_ground = models.ForeignKey(PlayGround, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"{self.member} - {self.play_ground} - {self.date}"


class CenterAvailability(models.Model):
    status_data = ((0, "Available"), (1, "Booked"))
    type = models.IntegerField(default=0, choices=status_data)
    name = models.CharField(max_length=250)
    date = models.DateField()

    def __str__(self):
        return self.name
   

class GroundAvailability(models.Model):

    status_data = ((0, "Available"), (1,"Booked"))
    type = models.IntegerField(default=0, choices=status_data)
    name = models.CharField(max_length=250)
    date = models.DateField()

    def __str__(self):
        return self.name
