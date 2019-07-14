from django.db import models

class IP(models.Model):
    ipaddress = models.CharField(max_length=25)

    def __str__(self):
        return self.ipaddress
