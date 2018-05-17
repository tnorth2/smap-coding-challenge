from django.core.management.base import BaseCommand
import numpy as np
import csv

class Command(BaseCommand):
    help = 'import data'

    def handle(self, *args, **options):
        user_iDs = "../data/user_data.csv"

        with open(user_iDs,'r') as f:
            user_iter = csv.reader(f, delimiter = ',', quotechar = '"')
            user = [user for user in user_iter]
        aUser = np.asarray(user[1:])

        # Lists of arrays to share index with user iD
        laDatetime = []
        laConsump = []

        for i in range(len(aUser)):
            dest_file = "../data/consumption/" + aUser[i][0] +".csv"

            with open(dest_file,'r') as dest_f:
                data_iter = csv.reader(dest_f, delimiter = ',', quotechar = '"')
                data = [data for data in data_iter]

            aData = np.asarray(data[1:])
            laDatetime.append(aData[:,0].astype('datetime64'))
            laConsump.append(aData[:,1].astype(float))

        lData_all = [aUser, laDatetime, laConsump] #single list comprehension for all data
