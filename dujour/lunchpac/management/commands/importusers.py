import pymssql
import sys

from django.core.management.base import BaseCommand, CommandError
from dujour.lunchpac.models import User

class Command(BaseCommand):
    help = 'Imports users from an old LunchPac database'

    def add_arguments(self, parser):
        parser.add_argument('db_server')
        parser.add_argument('db_user')
        parser.add_argument('db_pass')
        parser.add_argument('db_name')

    def handle(self, *args, **options):
        # reset history
        User.objects.all().delete()

        # connect to lunchpac db
        conn = pymssql.connect(options['db_server'], options['db_user'], options['db_pass'], options['db_name'])
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        row = cursor.fetchone()

        # parse all order rows
        while row:
            user_id = row[0]
            name = row[1]
            username = row[2]
            email = row[4]
            admin = row[5]
            
            # creates the database record
            if user_id != '':
                new_record = User.objects.create(user_id=user_id,
                                                name=name,
                                                username=username,
                                                email=email,
                                                admin=admin,
                                                )

            # load next row
            row = cursor.fetchone()

        conn.close()
