import os

from django.conf import settings
from django.core.files.storage import FileSystemStorage, default_storage
from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, **options):
        call_command("loaddata", "polls", verbosity=0)
        #call_command("update_index", verbosity=0)
        #call_command("rebuild_references_index", verbosity=0)
        print( "Awesome. data is loaded..")