#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from pygithub3.services.base import Service


class Milestones(Service):
    """ Consume `Milestones API
    <http://developer.github.com/v3/issues/milestones>`_
    """

    def list(self, user=None, repo=None):
        """ Get a repository's issues

        :param str user: Username
        :param str repo: Repo Name
        :returns: A :doc:`result`
        """
        request = self.request_builder('issues.milestones.list', user=user, repo=repo)
        return self._get_result(request, **self._get_mimetype_as_header())

    def get(self, number, user=None, repo=None):
        """ Get a single milestone

        :param str user: Username
        :param str repo: Repo Name
        :param int number: Milestone number
        """
        request = self.request_builder('issues.milestones.get', user=user, repo=repo, number=number)
        return self._get(request)
