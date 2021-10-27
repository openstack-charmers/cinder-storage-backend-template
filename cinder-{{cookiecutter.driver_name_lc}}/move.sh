#!/bin/sh

mv $1/*.charm "$1/cinder-{{ cookiecutter.driver_name_lc }}.charm"
