import csv
from TboProject.models import ObjectLocations
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Load data from data.csv file'

    def handle(self, *args, **kwargs):
        data_file = 'TboProject/data/datacpy.csv'
        keys = ('name', 'activ', 'discLong', 'discShort', 'addres', 'oktmo', 'fcp', 'actions',
                'startBuild', 'endBuild', 'finValue', 'curator', 'telephone', 'workHours', 'email',
                'siteUrl', 'typeObject', 'typeSport', 'latitude', 'longitude',
                'photoUrl')  # the CSV columns we will gather data from.

        records = []
        with open(data_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                records.append({k: row[k] for k in keys})

        for record in records:
            if record['longitude'] != '' and record['oktmo'] != '':
                # add the data to the database
                ObjectLocations.objects.get_or_create(
                    name=record['name'],
                    activ=record['activ'],
                    discLong=record['discLong'],
                    discShort=record['discShort'],
                    addres=record['addres'],
                    oktmo=int(record['oktmo']),
                    fcp=record['fcp'],
                    actions=record['actions'],
                    startBuild=record['startBuild'],
                    endBuild=record['endBuild'],
                    finValue=int(record['finValue']),
                    curator=record['curator'],
                    telephone=record['telephone'],
                    workHours=record['workHours'],
                    email=record['email'],
                    siteUrl=record['siteUrl'],
                    typeObject=record['typeObject'],
                    typeSport=record['typeSport'],
                    latitude=float(record['latitude']),
                    longitude=float(record['longitude']),
                    photoUrl=record['photoUrl']

                )
