from ckan import plugins
from ckan.plugins import toolkit
from ckan.lib.plugins import DefaultTranslation


class ThemeTucPlugin(plugins.SingletonPlugin, DefaultTranslation):
    plugins.implements(plugins.IConfigurer)

    # IConfigurer

    def update_config(self, config):
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_public_directory(config, 'public')
        toolkit.add_resource('fanstatic', 'theme_tuc')
