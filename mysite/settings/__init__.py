from .base_settings import *

if os.environ.get('DJANGO_ENVIRONMENT') == "dev":
    from .dev_settings import *
else:
    from .prod_settings import *