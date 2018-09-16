# -*- coding: utf-8 -*-
import os

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root@localhost:3306/bbs'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.urandom(24)