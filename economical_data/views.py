from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from django.core.serializers import serialize
from django.shortcuts import render,redirect
import finnhub
from economical_data.models import GeneralFinancialData
from os import getenv
from .forms import SearchForm

finnhub_client = finnhub.Client(api_key=getenv("FINNHUB_API"))

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
 
def search_view(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results=finnhub_client.symbol_lookup(query)
            return render(request, 'search.html', {'form': form, 'results': results['result']})
    else:
        form = SearchForm()

    return render(request, 'search.html', {'form': form})


def info_view(request):
    symbol = request.GET.get('symbol')
    print(symbol)
    error_message = None
    try:
        info_data=finnhub_client.company_profile2(symbol=symbol)
        columns = info_data.keys() if info_data else []
    except finnhub.FinnhubAPIException:
        info_data=None
        error_message = "No information available. Please try different stock."
    return render(request, 'info.html', {'info_data': info_data,'error_message': error_message})

def turbines_page(request):
    return render(request, 'map.html')