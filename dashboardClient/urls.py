# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from . import views

urlpatterns = [
    # # Matches any html file
    # re_path(r'dashboard/^.*\.html', views.pages, name='pages'),
    #
    # # The home page
    # path('dashboard/', views.dashboard, name='dashboard'),
]
