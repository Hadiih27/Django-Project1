from django.db import models
from django.contrib.auth.models import User  

# transport/models.py
from django.contrib.auth import get_user_model
User = get_user_model()

class TransportSchedule(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True, 
        blank=True  
    )
    direction = models.CharField(max_length=10)
    time = models.CharField(max_length=100)


def __str__(self):
        return self.name


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transport_schedule = models.ForeignKey('TransportSchedule', on_delete=models.CASCADE)
    feedback_text = models.TextField()
    rating = models.IntegerField() 

    def __str__(self):
        return f"Feedback for transport {self.transport_schedule.id} by {self.user.username}"
