from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.models import get_duration, is_visit_long
from django.shortcuts import render


def passcard_info_view(request, passcode):
    
    passcard = Passcard.objects.get(passcode=passcode)
    visits = passcard.visit_set.all()
    this_passcard_visits = []
    for visit in visits:
        duration = get_duration(visit)
        is_strange = is_visit_long(visit, minutes=60)
        this_passcard_visits.append(
        {
            "entered_at": visit.entered_at,
            "duration": duration,
            "is_strange": is_strange,
        }    
        )

    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits,
    }
    return render(request, "passcard_info.html", context)
