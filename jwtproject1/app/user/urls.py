#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 14:04:16 2019

@author: sambhav
"""
from django.conf.urls import url
from app.user.views import UserRegistrationView
from app.user.views import UserLoginView

urlpatterns = [
    url('signup', UserRegistrationView.as_view()),
    url('signin', UserLoginView.as_view()),
    ]
