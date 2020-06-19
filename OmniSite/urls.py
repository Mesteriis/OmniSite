from django.contrib import admin, auth
from django.urls import path, include , re_path
from . import views as viewsOmniSite
from News import views as newsViews
from authentication import views as authViews
from dashboard import views as dashViews

from django.contrib.auth.views import LogoutView #from auth


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
    path('register/', authViews.register_user, name="register"),
    path('logout/', LogoutView.as_view(), name="logout"),

    # dashboard
    path('dashboard/page-user.html', dashViews.userPage, name='userPage'),
    path('dashboard/page-omnicomm.html', dashViews.extOmniComm, name='extOmniComm'),
    path('dashboard/page-wialon.html', dashViews.extWialon, name='extWialon'),
    path('dashboard/page-saveDrive.html', dashViews.saveDrive, name='safeDrive'),
    path('dashboard/', dashViews.dashboard, name='dashboard'),
    path('dashboard/user', dashViews.getUserSettings, name='userSettings'),

    path('dashboard-n/', dashViews.newDash, name='dashboard-new'),

    # admin
    path('admin/', admin.site.urls),

    # mail senf
    path('sendmail/send', viewsOmniSite.sendMail, name='sendMail'),
]
