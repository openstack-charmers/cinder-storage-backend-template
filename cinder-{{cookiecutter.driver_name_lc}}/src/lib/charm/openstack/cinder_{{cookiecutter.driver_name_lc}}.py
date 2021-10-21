import json

from ops.charm import CharmBase


class Cinder{{ cookiecutter.driver_name }}Charm(CharmBase):

    _stored = StoredState()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.framework.observe(self.on.install, self._on_install)
        self.framework.observe(self.on.config_changed, self._on_config)
        self.framework.observe(
            self.on.storage_backend_relation_joined,
            self._on_storage_backend)
        self.framework.observer(
            self.on.storage_backend_relation_changed,
            self._on_storage_backend)

    def _on_install(self, _):
        self.unit.status = ActiveStatus('Unit is ready')

    def _render_config(self, config, app_name):
        volume_driver = ''
        options = [
            ('volume_driver', volume_driver)
        ]
        return json.dumps({
            "cinder": {
                "/etc/cinder/cinder.confg": {
                    "sections": {app_name: options}
                }
            }
        })

    def _set_data(self, data, config, app_name):
        data['backend-name'] = config['volume-backend-name'] or app_name
        data['subordinate_configuration'] = self._render_config(
            config, app_name)

    def _on_config(self, event):
        config = dict(self.framework.model.config)
        rel = self.framework.model.relations.get('storage-backend')[0]
        app_name = self.framework.model.app.name
        for unit in self.framework.model.get_relation('storage-backend').units:
            self._set_data(rel.data[self.unit], config, app_name)

    def _on_storage_backend(self, event):
        self._set_data(
            event.relation.data[self.unit],
            self.framework.model.config,
            self.framework.model.app.name)
