#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from .base import Resource
from .users import User
from .pull_requests import PullRequest


class Milestone(Resource):

    _dates = ('created_at', )
    _maps = {'creator': User}

    def __str__(self):
        return '<Milestone (%s)>' % getattr(self, 'description', '')

class Label(Resource):
    def __str__(self):
        return '<Label (%s)>' % getattr(self, 'name', '')

class Issue(Resource):

    _dates = ('created_at', 'updated_at', )
    _maps = {'pull_request': PullRequest, 'milestone': Milestone, 'assignee': User, 'user': User}
    _collection_maps = {'labels': Label, }

    def __str__(self):
        return '<Issue (%s)>' % getattr(self, 'title', '')
