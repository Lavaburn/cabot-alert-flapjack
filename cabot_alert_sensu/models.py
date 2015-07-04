from django.db import models
from cabot.cabotapp.alert import AlertPlugin, AlertPluginUserData

class FlapjackAlert(AlertPlugin):
    name = "Flapjack"
    author = "Nicolas Truyens"

    def send_alert(self, service, users, duty_officers):
        """TODO"""
        
        
        
        
        
        return

class FlapjackAlertUserData(AlertPluginUserData):
    name = "Flapjack Plugin"
    #favorite_bone = models.CharField(max_length=50, blank=True)

