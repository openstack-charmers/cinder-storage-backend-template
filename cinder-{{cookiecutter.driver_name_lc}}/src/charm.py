#! /usr/bin/env python3

# Copyright 2021 Canonical Ltd
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


import logging

from ops.main import main
from ops_openstack.plugins.classes import CinderStoragePluginCharm

logger = logging.getLogger(__name__)


class Cinder{{cookiecutter.driver_name}}Charm(OSBaseCharm):

    PACKAGES = [
        '{{ cookiecutter.additional_package_name|default("cinder-common", true) }}']

    stateless = False
    active_active = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._stored.is_started = True

    def cinder_configuration(self, charm_config) -> 'list[tuple]':
        """Return the configuration to be set by the principal"""
        cget = charm_config.get

        volume_backend_name = cget(
            'volume-backend-name') or self.framework.model.app.name

        raw_options = [
            ('volume_backend_name', volume_backend_name),
        ]

        options = [(x, y) for x, y in raw_options if y]
        return options


if __name__ == '__main__':
    main(Cinder{{cookiecutter.driver_name}}Charm)
