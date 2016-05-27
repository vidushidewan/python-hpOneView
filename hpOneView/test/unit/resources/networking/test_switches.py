# -*- coding: utf-8 -*-
###
# (C) Copyright (2012-2016) Hewlett Packard Enterprise Development LP
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
###

import unittest

import mock

from hpOneView.connection import connection
from hpOneView.resources.networking.switches import Switches
from hpOneView.resources.resource import ResourceClient


class SwitchesTest(unittest.TestCase):
    def setUp(self):
        self.host = '127.0.0.1'
        self.connection = connection(self.host)
        self._switches = Switches(self.connection)

    @mock.patch.object(ResourceClient, 'get_by_uri')
    def test_get_statistics_called_once(self, mock_get_by_uri):
        self._switches.get_statistics('3518be0e-17c1-4189-8f81-83f3724f6155')

        uri = '/rest/switches/3518be0e-17c1-4189-8f81-83f3724f6155/statistics'

        mock_get_by_uri.assert_called_once_with(uri)

    @mock.patch.object(ResourceClient, 'get_by_uri')
    def test_get_statistics_with_portName(self, mock_get_by_uri):
        self._switches.get_statistics('3518be0e-17c1-4189-8f81-83f3724f6155', 'X1')

        uri = '/rest/switches/3518be0e-17c1-4189-8f81-83f3724f6155/statistics/X1'

        mock_get_by_uri.assert_called_once_with(uri)