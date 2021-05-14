from django.db import models
from django.utils.timezone import now


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= "leaved at " + str(self.leaved_at) if self.leaved_at else "not leaved"
        )

    
def get_duration(visit):

    if visit.leaved_at:
        duration = visit.leaved_at - visit.entered_at
    else:
        duration = now() - visit.entered_at
 
    return duration

    
def is_visit_long(visit, duration, minutes=60):

    seconds_per_minutes = minutes * 60
 
    if visit.leaved_at:
        if duration.seconds <= seconds_per_minutes:
            is_strange = False
        else:
            is_strange = True
    else:
        if duration.seconds <= seconds_per_minutes:
            is_strange = False
        else:
            is_strange = True
            
    return is_strange 