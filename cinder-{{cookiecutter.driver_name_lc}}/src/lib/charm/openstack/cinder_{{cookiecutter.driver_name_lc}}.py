import charms_openstack.charm
import charmhelpers.core.hookenv as ch_hookenv  # noqa

charms_openstack.charm.use_defaults("charm.default-select-release")


class Cinder{{ cookiecutter.driver_name }}Charm(
    charms_openstack.charm.CinderStoragePluginCharm
):

    # The name of the charm
    name = "cinder_{{ cookiecutter.driver_name_lc }}"

    # Package to determine application version. Use "cinder-common" when
    # the driver is in-tree of Cinder upstream.
    version_package = "{{ cookiecutter.additional_package_name|default("cinder-common", true) }}"

    # Package to determine OpenStack release name
    release_pkg = "cinder-common"

    # this is the first release in which this charm works
    release = "{{ cookiecutter.release }}"

    # List of packages to install
    packages = ["{{ cookiecutter.additional_package_name }}"]

    stateless = True

    # Specify any config that the user *must* set.
    mandatory_config = []

    def cinder_configuration(self):
        volume_driver = ""
        driver_options = [
            ("volume_driver", volume_driver),
            # Add config options that needs setting on cinder.conf
        ]
        return driver_options
