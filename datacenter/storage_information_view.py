import sys
import django
import datetime

from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import now


def storage_information_view(request):
    
    not_gone_people = Visit.objects.filter(leaved_at=None)

    non_closed_visits = []
    for people in not_gone_people:
        non_closed_visits.append(
        {
            "who_entered": people.passcard.owner_name,
            "entered_at": people.entered_at,
            "duration": now() - people.entered_at
        }
        )
    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
