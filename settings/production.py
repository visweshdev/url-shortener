import os
from .base import *  # noqa: F401, F403
from .base import env, BASE_DIR

DEBUG = False

# Uses DATABASE_URL env var if available
DATABASES = {
    'default': env.db('DATABASE_URL', default=f'sqlite:///{os.path.join(BASE_DIR, "db.sqlite3")}')
}
DATABASES['default']['CONN_MAX_AGE'] = 500
