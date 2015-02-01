from datetime import datetime
import pytz

from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import Biography, Event, Work
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.mail import EmailMessage


def home(request):
    test = 'test'
    return render_to_response('home.html', 
                            {"test":test},
                             RequestContext(request))
def about(request):
    biography = Biography.objects.all()[:1]
    return render_to_response('about.html', 
                            {"biography": biography},
                             RequestContext(request))
def work(request):
    works = Work.objects.all().order_by('-id')
    return render_to_response('work.html', 
                            {"works":works},
                             RequestContext(request))
def events(request):
    events = Event.objects.all()
    upcoming_list = []
    for event in events:
        upcoming_list.append(datetime.now(pytz.utc) < event.event_date)
    events_and_upcoming = zip(events, upcoming_list)
    return render_to_response('events.html', 
                            {"events_and_upcoming": events_and_upcoming},
                             RequestContext(request))
def blog(request):
    test = 'test'
    return render_to_response('blog.html', 
                            {"test":test},
                             RequestContext(request))

def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            email = EmailMessage(
                request.POST['subject'], 
                request.POST['message'],
                request.POST.get('email', 'asmoor@gmail.com'),
                ['asmoor@gmail.com']
            )
            email.send()

    return render_to_response('contact.html', 
                            {"errors":errors},
                             RequestContext(request))
