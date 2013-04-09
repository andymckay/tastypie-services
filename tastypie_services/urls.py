from django.conf import settings

from tastypie.api import Api

from solitude.base import handle_500
from services import ErrorResource, SettingsResource, StatusResource


services = Api(api_name='services')
services.register(ErrorResource(set_handler=handle_500))
if getattr(settings, 'CLEANSED_SETTINGS_ACCESS', False):
    services.register(SettingsResource())
services.register(StatusResource())
