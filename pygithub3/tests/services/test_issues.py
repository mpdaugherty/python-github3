#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import requests
from mock import patch, Mock

from pygithub3.tests.utils.core import TestCase
from pygithub3.resources.base import json
from pygithub3.services.issues import Issue, Milestones
from pygithub3.tests.utils.base import (mock_response, mock_response_result,
                                        mock_json)
from pygithub3.tests.utils.services import _

json.dumps = Mock(side_effect=mock_json)
json.loads = Mock(side_effect=mock_json)

@patch.object(requests.sessions.Session, 'request')
class TestIssueService(TestCase):

    def setUp(self):
        self.issues = Issue()

    def test_LIST_without_user(self, request_method):
        request_method.return_value = mock_response_result()
        self.issues.list().all()
        self.assertEqual(request_method.call_args[0],
            ('get', _('issues')))

@patch.object(requests.sessions.Session, 'request')
class TestMilestonesService(TestCase):
    def setUp(self):
        self.ms = Milestones()

    def test_LIST_with_user_and_repo(self, request_method):
        request_method.return_value = mock_response_result()
        self.ms.list(user='octocat', repo='Hello-World').all()
        self.assertEqual(request_method.call_args[0],
            ('get', _('repos/octocat/Hello-World/milestones')))

    def test_LIST_with_state(self, request_method):
        request_method.return_value = mock_response_result()
        self.ms.list(user='octocat', repo='Hello-World', state='closed').all()
        self.assertEqual(request_method.call_args[0],
            ('get', _('repos/octocat/Hello-World/milestones')))

    def test_GET(self, request_method):

        request_method.return_value = mock_response_result()
        self.ms.get(user='octocat', repo='Hello-World', number=1)
        self.assertEqual(request_method.call_args[0],
            ('get', _('repos/octocat/Hello-World/milestones/1')))
