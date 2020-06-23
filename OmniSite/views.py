from django.shortcuts import render, Http404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
import json
from django.core.mail import send_mail

from django.views import generic
from braces.views import LoginRequiredMixin


def index(request):
    template = 'index.html'
    content = {

    }
    return render(request, 'index.html', content)


def signIn(request):
    template = 'SignIn.html'
    content = {

    }
    return render(request, template, content)


def joinAs(request):
    template = 'join.html'
    content = {

    }
    return render(request, template, content)


@csrf_exempt  # FIXME исправить коректность токена
def sendMail(request):

    jsObj = json.loads(request.body)
    pack = {
        'dep': jsObj['dep'],
        'type': jsObj['type'],
        'title': jsObj['title'],
        'note': jsObj['note'],
        'person': json.loads(jsObj['person']),
        'src': json.loads(jsObj['src']),
        'time': jsObj['time'],
        'isObserv': jsObj['isObserv'],
    }
    # https://docs.djangoproject.com/en/3.0/topics/email/
    send_mail(
        'Беда',
        jsObj['title'] + " - " + jsObj['note'],
        'a.meshcheryakov@omnicomm.pro',
        ['avm@sh-inc.ru'],
        fail_silently=False,
    )
    print('send')
    # template = ''
    # print (pack['src'])
    content = {

    }
    # print(request)
    return HttpResponse(request, content)
