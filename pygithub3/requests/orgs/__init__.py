# -*- encoding: utf-8 -*-

from pygithub3.requests.base import Request, ValidationError
from pygithub3.resources.orgs import Org

class List(Request):

    uri = 'user/{user}/orgs'
    resource = Org

    def clean_uri(self):
        if not self.user:
            return 'user/orgs'
