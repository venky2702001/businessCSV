from django.shortcuts import render
from django.http import HttpResponse
from CSV.models import *
import csv
# Create your views here.

def BEdata(request):
    with open('C:\\Users\\DELL\\OneDrive\\Desktop\\Django\\madhu\\Scripts\\businessCSV\\CSV\\Business-employment-data-september-2022-quarter-csv.csv','r') as FO:
        BED=csv.reader(FO)
        next(BED)
        for row in BED:
            BO=BusinessEmploymentData(series_reference=row[0],Period=row[1],Data_value=row[2],Suppressed=row[3],STATUS=row[4],UNITS=row[5],Magnitude=row[6],Subject=row[7],Group=row[8],Series_title_1=row[9],Series_title_2=row[10],Series_title_3=row[11],Series_title_4=row[12])
            BO.save()
        return HttpResponse('data is inserted')