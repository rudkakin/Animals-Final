from django.shortcuts import render
from .models import*
import pandas as pd
import mimetypes
import os
from django.views import View
from django.http.response import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import*
import pandas as pd
import json
import openpyxl


# Create your views here.
class home:
    def home(request):
        r = pd.read_csv('output.csv')
        df=pd.DataFrame(r)
        mydict={
            "df": df.to_html()
        }
    
        return render(request, 'index.html', context=mydict)
    def file(request):
        item = Animals.objects.all().values()
        df = pd.DataFrame(item)
        df= df.sort_values(by='Size', ascending=False)
        df.to_csv("output.csv")
        fileObj = open('output.csv','rb')
        response = HttpResponse(fileObj, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="Animals.csv"'
        return(response)

class Api(APIView):
    def get(self, request):
        r = pd.read_csv('output.csv')
        df=pd.DataFrame(r)
        t = df.to_dict()
        return Response(t)