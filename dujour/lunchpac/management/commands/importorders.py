import pymssql
import sys

from django.core.management.base import BaseCommand, CommandError
from dujour.lunchpac.models import Order

class Command(BaseCommand):
    help = 'Imports orders from an old LunchPac database'

    def add_arguments(self, parser):
        parser.add_argument('db_server')
        parser.add_argument('db_user')
        parser.add_argument('db_pass')
        parser.add_argument('db_name')

    def handle(self, *args, **options):
        # reset history
        Order.objects.all().delete()

        # connect to lunchpac db
        conn = pymssql.connect(options['db_server'], options['db_user'], options['db_pass'], options['db_name'])
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM orders')
        row = cursor.fetchone()

        # parse all order rows
        while row:
            order_id = row[0]
            user_id = row[1]
            order_item = row[2] # main order field
            add_date = row[16]
            restaurant_id = row[17]
            comments = []
            for i in range(3,14): # all the extra instructions fields
                if row[i] != '':
                    comments.append(row[i])
            comments_joined = ', '.join(comments)

            # handles when people leave the main field blank + put the order in some other field
            if order_item == '':
                order_item = comments_joined[:100]
                comments_joined = ''

            # creates the database record
            if order_item != '':
                new_record = Order.objects.create(order_id=order_id,
                                                user_id=user_id,
                                                order_item=order_item,
                                                comments=comments_joined,
                                                add_date=add_date,
                                                restaurant_id=restaurant_id,
                                                )

            # load next row
            row = cursor.fetchone()

        conn.close()