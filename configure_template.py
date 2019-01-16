#!/usr/bin/env python3

import argparse
import subprocess
import os
import shutil
from string import Template

RENAME_FILES = [
    ('src/lib/charm/openstack/cinder_STORAGE_NAME_LC.py',
     'src/lib/charm/openstack/cinder_{driver_name_lc}.py'),
    ('src/reactive/cinder_STORAGE_NAME_LC_handlers.py',
     'src/reactive/cinder_{driver_name_lc}_handlers.py'),
    ('src/tests/tests_cinder_STORAGE_NAME_LC.py',
     'src/tests/tests_cinder_{driver_name_lc}.py'),
    ('unit_tests/test_lib_charm_openstack_cinder_STORAGE_NAME_LC.py',
     'unit_tests/test_lib_charm_openstack_cinder_{driver_name_lc}.py'),
    ('target_tox.ini', 'tox.ini')]

REMOVE_FILES = [
    'README.md']

INTERFACES = [
    ('https://github.com/openstack-charmers/interface-cinder-backend.git', 'interface-cinder-backend')]

def get_context():
    ctxt = {}
    ctxt['driver_name'] = input("What is the name of the storage driver (init capped)?\n")
    ctxt['release'] = input("What is the earliest openstack release supported by the charm?\n").lower()
    ctxt['package_name'] = input("What is the name of the package containing the storage driver?\n").lower()
    ctxt['driver_name_lc'] = ctxt['driver_name'].lower()
    return ctxt

def rename_src_files(ctxt):
    for rename in RENAME_FILES:
        if os.path.isfile(rename[0]):
            shutil.move(rename[0], rename[1].format(**ctxt))

def update_template(filename, ctxt):
    with open(filename, 'r') as f:
        contents=f.read()

    contents = Template(contents).safe_substitute(ctxt)

    with open(filename, "w") as f:
        f.write(contents)

def update_templates(ctxt):
    for top_dir in ['src', 'unit_tests']:
        for dname, dirs, files in os.walk(top_dir):
            for fname in files:
                update_template(os.path.join(dname, fname), ctxt)

def remove_files():
    for f in REMOVE_FILES:
        if os.path.isfile(f):
            os.unlink(f)

def branch_interfaces():
    if not os.path.isdir('interfaces'):
        os.mkdir('interfaces')
    for interface in INTERFACES:
        target_dir = 'interfaces/{}'.format(interface[1])
        if not os.path.isdir(target_dir):
            subprocess.check_call(['git', 'clone', interface[0], target_dir])
        
def parse_args():
    parser = argparse.ArgumentParser(description='Run template configuration.')
    parser.add_argument('--branch-interfaces', dest='branch_interfaces', action='store_true')
    parser.set_defaults(branch_interfaces=False)
    return parser.parse_args()

def main():
    args = parse_args()
    ctxt = get_context()
    remove_files()
    update_templates(ctxt)
    rename_src_files(ctxt)
    if args.branch_interfaces:
        branch_interfaces()

if __name__ == '__main__':
      # execute only if run as a script
      main()
