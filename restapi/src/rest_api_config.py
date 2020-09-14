import os


class config:

    debugging = int(os.environ['CONFIG_USE_DEBUG_MODE'])
    CONFIG_HTTP_USE_TLS         = False
    CONFIG_HTTP_HOST            = "localhost"
    CONFIG_HTTP_PORT            = 8000
    CONFIG_HTTP_TLS_PORT        = 443
