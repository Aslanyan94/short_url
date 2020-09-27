import string
import random

from django.conf import settings


def random_string():
    length = random.randrange(*settings.SHORT_URL_LENGTH_BOUNDS)
    possible_options = string.digits + string.ascii_lowercase
    return ''.join(random.choice(possible_options) for _ in range(length))