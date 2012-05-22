#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from pygithub3.services.base import Service


class Org(Service):
    """ Consume `Orgs API <http://developer.github.com/v3/orgs>`_ """

    def __init__(self, **config):
        super(Org, self).__init__(**config)

    def list(self, user=None):
        """ Get user's orgs

        :returns: A :doc:`result`

        If you call it and you are authenticated, get the
        authenticated user's public/private orgs.

        If you are not authenticated, you only get the user's
        public orgs.

        ::
        """
        request = self.request_builder('orgs.list', user=user)
        return self._get_result(request)
