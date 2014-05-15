from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import Biography, Event, Media
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.mail import EmailMessage


def home(request):
    bio = biography()
    medias = media()
    events = event()

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

    return render_to_response('base.html', 
                            {"biography_text":bio['biography_text'],
                             "events":events['events'],
                             "medias":medias['media'],
                             "errors":errors},
                             RequestContext(request))


def biography():
    bio = Biography.objects.all()[0]
    if bio:
        text = bio.text
    else:
        text = ""
    return {"biography_text":text}


def event():
    events = Event.objects.all()
    return {"events":events}


def media():
    medias = Media.objects.all()[:3]
    return {"media":medias}


def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        # ContactForm was defined in the previous section
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    return render(request, 'contact.html', {
        'form': form,
    })

    