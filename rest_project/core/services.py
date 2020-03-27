import datetime
import hashlib

from django.utils.functional import SimpleLazyObject


def generate_api_key(user: SimpleLazyObject) -> str:
    """Генерирует API key."""
    salt = datetime.datetime.now().strftime('%d-%b-%Y%H:%M:%S.%f')
    h = hashlib.sha1(str(user).encode() + salt.encode())
    return h.hexdigest()
