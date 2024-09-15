from django.shortcuts import render
from django.http import HttpResponse
import datetime


def index(request):
    dt = datetime.datetime.now()
    current_hour = dt.hour
    greeting = None
    if current_hour >= 5 and current_hour < 12:
        greeting = 'Good Morning'
    elif current_hour >= 12 and current_hour < 17:
        greeting = 'Good Afternoon'
    elif current_hour >= 17 and current_hour < 21:
        greeting = 'Good Evening'
    else:
        greeting = 'Good Night'

    html_response = f"""
                        <h1>current time: {dt.hour}-{dt.minute}-{dt.second}</h1>
                        <h1>{greeting}</h1>
                    """

    return HttpResponse(f'{html_response}')
