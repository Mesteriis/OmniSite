from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from django.contrib.auth.models import User
import requests
from time import sleep





@login_required(login_url="/login/")
def dashboard(request):
    return render(request, "dashboard/dashboard.html")


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('dashboard/error-404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('dashboard/error-500.html')
        return HttpResponse(html_template.render(context, request))


def getUserSettings(request):
    res = User
    print(request)
    return HttpResponse(request, res)



def newDash(request):
    login = 'test1'
    password = 'test1'

    # омником
    # tokenOmniCom = requests.post('https://online.omnicomm.ru/auth/login?jwt=1',
    #                              json={
    #                                  'login': 'demo',
    #                                  'password': 'demo'
    #                              }).json()['jwt']

    # виалон
    url1 = 'http://online.wialon.center/login.html'
    url2 = 'http://online.wialon.center/oauth.html'
    jn1 = {
        'login': login,
        'password': password,
        'Content-Language': 'ru',
        'response_type': 'token',
    }
    # html = requests.get(url1, json=jn1).text
    # sign = html[html.find('sign') + 13:html.find('sign') + 13 + 44]
    # sleep(3)
    headers = {
        'User-Agent': 'My User Agent 1.0',
        'From': 'youremail@domain.com'  # This is another valid field
    }
    jn2 = {
        'content-type': 'application/x-www-form-urlencoded',
        'response_type': 'token',
        'client_id': 'wialon.center ГЛОНАСС мониторинг транспорта',
        'redirect_uri': 'http://online.wialon.center/login.html',
        'access_type': '0x100',
        'activation_time': '0',
        'duration': '0',  # 2592000
        'flags': '6',
        # 'sign': sign,
        'login': login,
        'passw': password,
        'Content-Language': 'ru'
    }
    # res = requests.post(url2, data=jn2)

    tokenWialon: str
    code_error: int

    # tokenWialon = res.url[res.url.find('access_token=') + 13:res.url.find('&svc_error')]
    # code_error = int(res.url[res.url.find('error=') + 6:len(res.url)])
    context = {
        # 'tokenOmniComm': tokenOmniCom,
        # 'tokenWialon': tokenWialon,
        # 'errorWialon': code_error,
    }
    template = 'dashboard/dashboard-new.html'

    return render(request, template, context)

def userPage(request):
    context = {}
    template = 'dashboard/page-user.html'

    return render(request, template, context)



def extOmniComm(request):
    context = {}
    template = 'dashboard/page-omnicom.html'

    return render(request, template, context)



def extWialon(request):
    context = {}
    template = 'dashboard/page-wialon.html'

    return render(request, template, context)



def saveDrive(request):
    context = {}
    template = 'dashboard/page-saveDrive.html'

    return render(request, template, context)