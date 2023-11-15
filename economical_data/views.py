from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from django.core.serializers import serialize
from django.shortcuts import render

from economical_data.models import GeneralFinancialData

def get_ECB_DF(request):
    try:
        filtered_rows = GeneralFinancialData.objects.filter(
            TITLE="ECB Deposit facility - date of changes (raw data) - Level"
        )
        
        # Convert OBS_VALUE to float and round to 2 decimal places
        for row in filtered_rows:
            row.OBS_VALUE = round(float(row.OBS_VALUE), 2)

        json_data = serialize('json', filtered_rows)
        return JsonResponse({'data': json_data})
    except GeneralFinancialData.DoesNotExist:
        return JsonResponse({'error': 'No data available'}, status=404)
    
def get_ECB_MLF(request):
    try:
        filtered_rows = GeneralFinancialData.objects.filter(
            TITLE="ECB Marginal lending facility - date of changes (raw data) - Level"
        )
        
        # Convert OBS_VALUE to float and round to 2 decimal places
        for row in filtered_rows:
            row.OBS_VALUE = round(float(row.OBS_VALUE), 2)

        json_data = serialize('json', filtered_rows)
        return JsonResponse({'data': json_data})
    except GeneralFinancialData.DoesNotExist:
        return JsonResponse({'error': 'No data available'}, status=404)
    
def get_ECB_MRO(request):
    try:
        filtered_rows = GeneralFinancialData.objects.filter(
            TITLE="ECB Main refinancing operations - fixed rate tenders (fixed rate) (date of changes) - Level"
        )
        
        # Convert OBS_VALUE to float and round to 2 decimal places
        for row in filtered_rows:
            row.OBS_VALUE = round(float(row.OBS_VALUE), 2)

        json_data = serialize('json', filtered_rows)
        return JsonResponse({'data': json_data})
    except GeneralFinancialData.DoesNotExist:
        return JsonResponse({'error': 'No data available'}, status=404)

def display_page(request):
    return render(request, 'rates.html')

def front_page(request):
    return render(request, 'index.html')