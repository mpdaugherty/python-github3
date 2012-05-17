#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from .base import Resource
from .users import User


class Issue(Resource):

    _dates = ('created_at', 'updated_at', )
    _maps = {'pull_request': ..., 'milestone': Milestone, 'assignee': User, 'user': User}
    _collection_maps = {'labels': ..., }

    def __str__(self):
        return '<Issue (%s)>' % getattr(self, 'title', '')

class Milestone(Resource):

    _dates = ('created_at', )
    _maps = {'creator': User}

    def __str__(self):
        return '<Milestone (%s)>' % getattr(self, 'description', '')
