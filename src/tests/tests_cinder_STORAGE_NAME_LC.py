#!/usr/bin/env python3

# Copyright 2019 Canonical Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Encapsulate cinder-${driver_name_lc} testing."""

import logging

import zaza.model
import zaza.charm_tests.test_utils as test_utils


class Cinder${driver_name}Test(test_utils.OpenStackBaseTest):
    """Encapsulate ${driver_name} tests."""

    @classmethod
    def setUpClass(cls):
        """Run class setup for running tests."""
        super(Cinder${driver_name}Test, cls).setUpClass()

    def test_${driver_name_lc}(self):
        """foo."""
        logging.info('${driver_name_lc}')
        expected_contents = {
            'cinder-${driver_name_lc}': {
                'iscsi_helper': ['tgtadm'],
                'volume_dd_blocksize': ['512']}}

        zaza.model.run_on_leader(
            'cinder',
            'sudo cp /etc/cinder/cinder.conf /tmp/',
            model_name=self.model_name)
        zaza.model.block_until_oslo_config_entries_match(
            'cinder',
            '/tmp/cinder.conf',
            expected_contents,
            model_name=self.model_name,
            timeout=2)
