import sys
import argparse
import csv

from django.core.management.base import BaseCommand, CommandError
from userprofile.tools import collapse_complex_key
from webapi.serializers import UserProfileSerializer


class Command(BaseCommand):

    """
    Sample CSV must be with heasers like this below
    user.password;user.is_superuser;user.first_name;user.last_name;user.email;gender;age;pet;user.username

    """
    help = 'Add users from file'

    def add_arguments(self, parser):
        parser.add_argument(
            '--filename',
            type=argparse.FileType('r'),
            default=sys.stdin
        )
        parser.add_argument('--delimiter')

    def handle(self, *args, **options):
        filename = options.get('filename')
        delimiter = options.get('delimiter')
        if not filename and not delimiter:
            self.stdout.write(
                self.style.ERROR('You must give file name or delimiter')
            )
            return

        spamreader = csv.DictReader(filename, delimiter=delimiter)
        for row in spamreader:
            serializer = UserProfileSerializer(data=collapse_complex_key(row))
            if serializer.is_valid():
                serializer.save()
                self.stdout.write(
                    self.style.SUCCESS('Successfully saved user {}'.format(
                        row.get('user.username')))
                )
            else:
                self.stdout.write(
                    self.style.ERROR('Error while saving user {}'.format(
                        row.get('user.username')
                    ))
                )

