from django.db import models

class Room(models.Model):
    possible_room_types = [('KS', 'King Smoking'), ('KNS', 'King Non-Smoking')]
    num = models.CharField(max_length=5)
    room_type = models.CharField(choices=possible_room_types, max_length=3, default=None)
    check_out = models.BooleanField(default=True)

    class Meta:
        db_table = "room"