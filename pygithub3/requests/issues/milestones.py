# -*- encoding: utf-8 -*-

from pygithub3.requests.base import Request
from pygithub3.resources.issues import Milestone

class List(Request):

    uri = 'issues/{user}/{repo}/milestones'
    resource = Milestone


class Get(Request):

    uri = 'issues/{user}/{repo}/milestones/{number}'
    resource = Milestone
