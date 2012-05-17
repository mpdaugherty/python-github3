# -*- encoding: utf-8 -*-

from pygithub3.requests.base import Request, ValidationError
from pygithub3.resources.issues import Issue

class List(Request):

    uri = 'issues'
    resource = Issue
