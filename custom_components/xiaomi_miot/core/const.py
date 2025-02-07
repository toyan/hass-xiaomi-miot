from .device_customizes import DEVICE_CUSTOMIZES
from .miot_local_devices import MIOT_LOCAL_MODELS  # noqa
from .translation_languages import TRANSLATION_LANGUAGES  # noqa

DOMAIN = 'xiaomi_miot'
DEFAULT_NAME = 'Xiaomi Miot'

CONF_MODEL = 'model'
CONF_XIAOMI_CLOUD = 'xiaomi_cloud'
CONF_SERVER_COUNTRY = 'server_country'
CONF_CONN_MODE = 'conn_mode'
CONF_CONFIG_VERSION = 'config_version'

DEFAULT_CONN_MODE = 'cloud'

SUPPORTED_DOMAINS = [
    'sensor',
    'binary_sensor',
    'switch',
    'light',
    'fan',
    'climate',
    'cover',
    'humidifier',
    'media_player',
    'camera',
    'vacuum',
    'water_heater',
    'device_tracker',
    'remote',
    'alarm_control_panel',
]

CLOUD_SERVERS = {
    'cn': 'China',
    'de': 'Europe',
    'i2': 'India',
    'ru': 'Russia',
    'sg': 'Singapore',
    'us': 'United States',
}

try:
    # hass 2020.12.2
    from homeassistant.components.number import DOMAIN as DOMAIN_NUMBER
    SUPPORTED_DOMAINS.append(DOMAIN_NUMBER)
except (ModuleNotFoundError, ImportError):
    DOMAIN_NUMBER = None

try:
    # hass 2021.6
    from homeassistant.components.sensor import STATE_CLASS_MEASUREMENT
except (ModuleNotFoundError, ImportError):
    STATE_CLASS_MEASUREMENT = None

try:
    # hass 2021.7
    from homeassistant.components.select import DOMAIN as DOMAIN_SELECT
    SUPPORTED_DOMAINS.append(DOMAIN_SELECT)
except (ModuleNotFoundError, ImportError):
    DOMAIN_SELECT = None

try:
    # hass 2021.9
    from homeassistant.components.sensor import STATE_CLASS_TOTAL_INCREASING
except (ModuleNotFoundError, ImportError):
    STATE_CLASS_TOTAL_INCREASING = None

try:
    # hass 2021.11
    from homeassistant.const import ENTITY_CATEGORY_CONFIG, ENTITY_CATEGORY_DIAGNOSTIC
except (ModuleNotFoundError, ImportError):
    ENTITY_CATEGORY_CONFIG = None
    ENTITY_CATEGORY_DIAGNOSTIC = None

try:
    # hass 2021.12
    from homeassistant.components.button import DOMAIN as DOMAIN_BUTTON
    SUPPORTED_DOMAINS.append(DOMAIN_BUTTON)
except (ModuleNotFoundError, ImportError):
    DOMAIN_BUTTON = None


GLOBAL_CUSTOMIZES = {
    'models': DEVICE_CUSTOMIZES,
}
