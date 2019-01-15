import charms_openstack.charm
import charmhelpers.core.hookenv as ch_hookenv # noqa 


class Cinder${driver_name}Charm(
        charms_openstack.charm.CinderStoragePluginCharm):

    name = 'cinder_${driver_name_lc}'
    version_package = '${package_name}'
    release = '${release}'
    packages = [version_package]
    stateless = True

    def cinder_configuration(self):
        volume_driver = ''
        driver_options = [
            ('volume_driver', volume_driver),
            # Add config options that needs setting on cinder.conf
        ]
        return driver_options
