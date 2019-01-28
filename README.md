Using template to create a storage backend.
===========================================

1) Clone template:
------------------

```
sudo apt -y install cookiecutter
cookiecutter https://github.com/openstack-charmers/cinder-storage-backend-template
```

2) Edit src/config.yaml
-----------------------

- In the src/config.yaml add any options that should be configurable by the
  user. In most cases this is details for connecting to the storage array.
  Where appropriate the charm will pass these to the cinder principle charm
  for inclusion in cinder.conf.
- If the storage driver is to be installed from a ppa then uncomment the
  driver-* options, otherwise delete them.
 
3) Update 'cinder\_configuration' in src/lib/charm/openstack/cinder_*
--------------------------------------------------------------------

The 'cinderr\_configuration' method controls configuration options are sent to
the principle cinder charm for inclusion in cinder.conf. For example:

If a 'superarray' driver was being configured in step 3 and
superarray-username, superarray-password and superarray-hostname config
options were added to config.yaml and the array needs driver XXX then
'cinder\_configuration' might look like:

    def cinder_configuration(self):
        volume_driver = 'cinder.volume.drivers.ARRAYVENDOR.iscsi.ARRAYISCSIDriver'
        driver_options = [
            ('volume_driver', volume_driver),
            ('username', self.config.get('superarray-username')),
            ('password', self.config.get('superarray-password')),
            ('hostname', self.config.get('superarray-hostname'))]
        return driver_options
 
Which will result in the following section being added to cinder.conf:

        [cinder-superarray]
        volume_driver = cinder.volume.drivers.ARRAYVENDOR.iscsi.ARRAYISCSIDriver
        username = root
        password = password
        hostname = 10.5.0.13

4) Update unit tests
--------------------

Edit unit\_tests/test\_lib\_charm\_openstack\_cinder\* and update unit
tests.

5) Update functional tests
--------------------------

Update the bundles in tests/bundles/\*yaml as needed and edit
tests\/tests\_cinder\_\*py to add functional testing.

TODO:
-----
- Add basic zaza tests
- Add unit tests
  * Add skeleton readme for generated charm
