from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone

import requests


class Command(BaseCommand):
    help = "run for creating specified count user"

    def add_arguments(self, parser):
        parser.add_argument('user count', type=int)

    def handle(self, *args, **options):
        param = options.get("user count")
        users_info = requests.get(
            url="https://randomuser.me/api/?results={}&inc=name,login,email&nat=us,gb&noinfo".format(param)
            ).json()["results"]

        for user_credential in users_info:
            User.objects.create_user(
                first_name=user_credential["name"]["first"],
                last_name=user_credential["name"]["last"],
                email=user_credential["email"],
                username=user_credential["login"]["username"],
                password=user_credential["login"]["password"],
                date_joined=timezone.now())

        print("{} user account was created".format(param))