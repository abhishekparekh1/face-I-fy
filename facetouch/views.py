from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from facetouch.models import Event
from datetime import datetime


@csrf_exempt
def create_event(request):
    if request.method == 'POST':
        # import pdb;pdb.set_trace()
        data = json.loads(request.body)
        event = Event(event_name=data['event_name'], time_stamp=datetime.utcnow())
        event.save()
    return JsonResponse({'status': 200})


def get_event(request):
    if request.method == 'GET':
        events = Event.objects.all()
        for event in events:
            if not event.is_consumed:
                event.is_consumed = True
                event.save()
                return JsonResponse({"event_name": event.event_name, "timestamp": event.time_stamp})

    return JsonResponse({'status': 'no new event'})
