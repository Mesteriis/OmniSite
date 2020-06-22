from django.contrib import admin, auth
from django.urls import path, include, re_path
from . import views as viewsOmniSite
from News import views as newsViews
from authentication import views as authViews
from dashboardClient import views as dashViews

from django.contrib.auth.views import LogoutView #from auth
from django_private_chat import urls as django_private_chat_urls # Chat

urlpatterns = [
    # Site
    path('', viewsOmniSite.index, name='index'),
    path('join/', viewsOmniSite.joinAs, name='joniAs'),

    # news
    path('news/', newsViews.newsListView.as_view(), name='News'),
    path('news/detail/<int:pk>', newsViews.detailNewsView.as_view(), name='detail'),
    path('news/adminNews/', newsViews.admNews, name='adminNews'),

    # auth
    path('login/', authViews.login_view, name="login"),
    # path('register/', authViews.register_user, name="register"),
    path('logout/', LogoutView.as_view(), name="logout"),

    # dashboard
    path('dashboardClient/', dashViews.dashboard, name='dashboardClient'),

    # admin
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('admin/', admin.site.urls),

    # Chat
    path('chat/', include('django_private_chat.urls')),

    # mail senf
    path('sendmail/send', viewsOmniSite.sendMail, name='sendMail'),
]
