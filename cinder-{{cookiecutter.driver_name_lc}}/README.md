{{ cookiecutter.driver_name }} Storage Backend for Cinder
-------------------------------

Overview
========

This charm provides a {{ cookiecutter.driver_name }} storage backend for use with the Cinder
charm.

To use:

    juju deploy cinder
    juju deploy cinder-{{ cookiecutter.driver_name_lc }}
    juju add-relation cinder-{{ cookiecutter.driver_name_lc }} cinder

Configuration
=============

See config.yaml for details of configuration options.
