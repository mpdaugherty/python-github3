# -*- encoding: utf-8 -*-

from pygithub3.requests.base import Request
from pygithub3.resources.issues import Milestone

class List(Request):

    uri = 'repos/{user}/{repo}/milestones'
    resource = Milestone


class Get(Request):

    uri = 'repos/{user}/{repo}/milestones/{number}'
    resource = Milestone
