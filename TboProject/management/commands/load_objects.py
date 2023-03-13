import csv

from django.core.management.base import BaseCommand

from TboProject.models import ObjectLocations


class Command(BaseCommand):
    help = 'Load data from data.csv file'

    def handle(self, *args, **kwargs):
        with open('data.csv', 'r', encoding='UTF-8') as f:
            reader = csv.reader(f, delimiter=';')
            header = next(reader)
            for i in reader:
                row = {}
                for index, value in enumerate(i):
                    row[header[index]] = value
                try:
                    ObjectLocations.objects.get_or_create(**row)
                except ValueError:
                    continue
