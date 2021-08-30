from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt


# Create your views here.

def welcome(request):
    return render(request,'welcome.html')

def news_of_day(request):
    date = dt.date.today()
    return render(request, 'all-news/today_news.html', {"date": date,})

    # #Funtion to convert date object to find the exact day
    # day = convert_dates(date)
    # html = f'''
    #     <html>
    #         <body>
    #             <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
    #         </body>
    #     </html>        
    #         '''   
    # return HttpResponse(html) 

# def convert_dates(dates):

#     #Function that gets the weekday number for the date.
#     day_number = dt.date.weekday(dates)

#     days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

#     #returning the actual day of the week
#     day = days[day_number]   
#     return day         

def past_days_news(request,past_date):

    try:
        #Converts data from the string Url
        
        date  = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        #Raise 404 error when VauleError is thrown
        raise Http404() 
        assert False

    if date == dt.date.today():
        return redirect(news_of_day)

    return render(request, 'all-news/past_news.html',{"date": date})        
            

    # day  = convert_dates(date)
    # html = f'''
    #     <html>
    #         <body>
    #             <h1> News for {day} {date.day}-{date.month}-{date.year}</h1>
    #         </body>
    #     </html>        
    #          '''
    # return HttpResponse(html)         