# -*- coding: utf-8 -*-

from flask import Blueprint

bp = Blueprint('front', __name__, url_prefix='/')


@bp.route('/')
def index():
    return 'front World!'
