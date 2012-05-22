#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import requests
from mock import patch, Mock

from pygithub3.tests.utils.core import TestCase
from pygithub3.resources.base import json
from pygithub3.services.orgs import Org
from pygithub3.tests.utils.base import (mock_response, mock_response_result,
                                        mock_json)
from pygithub3.tests.utils.services import _

json.dumps = Mock(side_effect=mock_json)
json.loads = Mock(side_effect=mock_json)

@patch.object(requests.sessions.Session, 'request')
class TestOrgsService(TestCase):

    def setUp(self):
        self.orgs = Org()

    def test_LIST_without_user(self, request_method):
        request_method.return_value = mock_response_result()
        self.orgs.list().all()
        self.assertEqual(request_method.call_args[0],
            ('get', _('user/orgs')))

    def test_LIST_with_user(self, request_method):
        request_method.return_value = mock_response_result()
        self.orgs.list(user='octocat').all()
        self.assertEqual(request_method.call_args[0],
            ('get', _('user/octocat/orgs')))
