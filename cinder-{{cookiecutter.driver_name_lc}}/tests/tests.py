#!/usr/bin/env python3

# Copyright 2022 Canonical Ltd.
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

"""Encapsulate cinder-{{ cookiecutter.driver_name_lc }} testing."""

from zaza.openstack.charm_tests.cinder_backend.tests import CinderBackendTest


class Cinder{{cookiecutter.driver_name}}Test(CinderBackendTest):
    """Encapsulate {{ cookiecutter.driver_name }} tests."""

    backend_name = '{{ cookiecutter.driver_name }}'

    expected_config_content = {
        '{{ cookiecutter.driver_name }}': {
            'volume-backend-name': ['{{ cookiecutter.driver_name }}'],
        }}
