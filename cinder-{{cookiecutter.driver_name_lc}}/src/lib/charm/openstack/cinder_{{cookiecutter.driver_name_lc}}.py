import charms_openstack.charm
import charmhelpers.core.hookenv as ch_hookenv  # noqa

charms_openstack.charm.use_defaults('charm.default-select-release')


class Cinder{{ cookiecutter.driver_name }}Charm(
        charms_openstack.charm.CinderStoragePluginCharm):

    name = 'cinder_{{ cookiecutter.driver_name_lc }}'
    version_package = '{{ cookiecutter.package_name }}'
    release = '{{ cookiecutter.release }}'
    packages = [version_package]
    release_pkg = version_package
    stateless = True
    # Specify any config that the user *must* set.
    mandatory_config = []

    def cinder_configuration(self):
        volume_driver = ''
        driver_options = [
            ('volume_driver', volume_driver),
            # Add config options that needs setting on cinder.conf
        ]
        return driver_options


class Cinder{{ cookiecutter.driver_name }}CharmRocky(Cinder{{ cookiecutter.driver_name }}Charm):

    # Rocky needs py3 packages.
    release = 'rocky'
    version_package = '{{ cookiecutter.package3_name }}'
    packages = [version_package]
