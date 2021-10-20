# Copyright 2016 Canonical Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import
from __future__ import print_function

import charmhelpers

import charm.openstack.cinder_{{ cookiecutter.driver_name_lc }} as cinder_{{ cookiecutter.driver_name_lc }}

import charms_openstack.test_utils as test_utils


class TestCinder{{ cookiecutter.driver_name }}Charm(test_utils.PatchHelper):
    def _patch_config_and_charm(self, config):
        self.patch_object(charmhelpers.core.hookenv, "config")

        def cf(key=None):
            if key is not None:
                return config[key]
            return config

        self.config.side_effect = cf
        c = cinder_{{ cookiecutter.driver_name_lc }}.Cinder{{ cookiecutter.driver_name }}Charm()
        return c

    def test_cinder_base(self):
        charm = self._patch_config_and_charm({})
        self.assertEqual(charm.name, "cinder_{{ cookiecutter.driver_name_lc }}")
        self.assertEqual(charm.version_package, "{{ cookiecutter.additional_package_name|default("cinder-common", true) }}")
        self.assertEqual(charm.packages, ["{{ cookiecutter.additional_package_name }}"])

    def test_cinder_configuration(self):
        charm = self._patch_config_and_charm({"a": "b"})
        config = charm.cinder_configuration()  # noqa
        # Add check here that configuration is as expected.
        # self.assertEqual(config, {})
