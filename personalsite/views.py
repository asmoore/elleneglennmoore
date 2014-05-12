from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import Biography, Event, Media
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.mail import EmailMessage


def home(request):
    bio = biography()
    poem = poems()
    media_item = media()
    event_list = events()

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
                             "events":event_list['events'],
                             "media_item":media_item,
                             "errors":errors},
                             RequestContext(request))

def biography():
    bio = Biography.objects.all()[0]
    if bio:
        text = bio.text
    else:
        text = ""
    return {"biography_text":text}

def poems():
    poem_title = "Ode to Ipsum"
    poem_text = """
Lorem ipsum dolor sit amet,
consectetur adipisicing elit, 
sed do eiusmod tempor incididunt 
ut 
labore et dolore magna aliqua. 
Ut 
enim ad minim veniam, 
quis nostrud exercitation 
ullamco laboris nisi ut aliquip ex ea commodo consequat."""
    return {"poem_title":poem_title,"poem_text":poem_text}

def events():
    events = Event.objects.all()
    return {"events":events}

def media():
    media = Media.objects.all()[:3]
    media_html = ""
    i = 1
    for media_item in media:
        if i == 1:
            li_number = "one"
        elif i == 2:
            li_number = "two"
        elif i ==3:
            li_number = "three"
        elif i ==4:
            li_number = "four"
        elif i ==5:
            li_number = "five"
        if media_item.media_type == "VI":
            media_html = media_html + """<li data-slidr="%s">
              <div class="jumbotron" id="media">
                %s
              </div>
            </li>""" % (li_number,media_item.media_text)
        elif media_item.media_type == "TX":
            media_html = media_html + """<li data-slidr="%s">
                %s
            </li>""" % (li_number,media_item.media_text)
        else: #Image
            media_html = media_html + """<li data-slidr="%s">
            <center><img src="/static/img/%s" alt="My image"></center>
          </li>""" % (li_number,media_item.media_text)
        i = i + 1
    
    return {"media":media_html}

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