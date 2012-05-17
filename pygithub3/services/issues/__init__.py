#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from pygithub3.services.base import Service
from milestones import Milestones


class Issue(Service):
    """ Consume `Issues API <http://developer.github.com/v3/issues>`_ """

    def __init__(self, **config):
        self.milestones = Milestones(**config)
        super(Issue, self).__init__(**config)

    def list(self):
        """ Get authenticated user's issues

        :returns: A :doc:`result`

        If you call it and you are authenticated, get the
        authenticated user's gists.

        ::

            gist_service.list()
        """
        request = self.request_builder('issues.list')
        return self._get_result(request)
