# -*- coding: utf-8 -*-

from flask import Blueprint

bp = Blueprint('common', __name__, url_prefix='/c')


@bp.route('/')
def index():
    return 'common World!'
