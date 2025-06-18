from django.db import models

# Create your models here.

class Feedback(models.Model):#new django model

    encryptedMsg = models.BinaryField()#to encrypt feedback message
    timestamp = models.DateTimeField(auto_now_add=True)#just for time shown when fb was submitted
    submitted_ip = models.GenericIPAddressField(null=True, blank=True)#ip address of user who submitted fb
    #ip is optinal if can't be captured// used to check for misuse

    def __str__(self):
        return f"feedback submitted at {self.timestamp}"
