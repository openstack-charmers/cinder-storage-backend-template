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


from ops_openstack.plugins.classes import CinderStoragePluginCharm
from ops_openstack.core import charm_class, get_charm_class_for_release
from ops.main import main


class CinderCharmBase(CinderStoragePluginCharm):

    PACKAGES = ['{{ cookiecutter.additional_package_name|default("cinder-common", true) }}']
    # Overriden from the parent. May be set depending on the charm's properties
    stateless = {{ cookiecutter.stateless }}
    active_active = {{ cookiecutter.active_active }}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def cinder_configuration(self, config):
        # Return the configuration to be set by the principal.
        backend_name = config.get('volume-backend-name',
                                  self.framework.model.app.name)
        volume_driver = ''
        options = [
            ('volume_driver', volume_driver),
            ('volume_backend_name', backend_name),
        ]

        if config.get('use-multipath'):
            options.extend([
                ('use_multipath_for_image_xfer', True),
                ('enforce_multipath_for_image_xfer', True)
            ])

        return options


@charm_class
class Cinder{{ cookiecutter.driver_name }}Charm(CinderCharmBase):
    release = '{{ cookiecutter.release }}'


if __name__ == '__main__':
    main(get_charm_class_for_release())
