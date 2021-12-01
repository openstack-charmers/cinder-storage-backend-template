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


import json


from ops_openstack.plugins.classes import BaseCinderCharm
from ops.framework import StoredState
from ops.main import main
from ops.model import ActiveStatus


class Cinder{{ cookiecutter.driver_name }}Charm(BaseCinderCharm):

    PACKAGES = ['{{ cookiecutter.additional_package_name|default("cinder-common", true) }}']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def cinder_configuration(self, config):
        # Return the configuration to be set by the principal.
        volume_driver = ''
        options = [
            ('volume_driver', volume_driver)
        ]
        return options


if __name__ == '__main__':
    main(Cinder{{ cookiecutter.driver_name }}Charm)
