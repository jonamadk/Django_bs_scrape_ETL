

from django.urls import path
from data.views import IndividualLiveTradingDataDetail, LiveTradingDataList
from data.scrape import task

urlpatterns = [

    path('data/',task ),
    path('articles/', LiveTradingDataList.as_view()),
    path('article/<int:pk>/', IndividualLiveTradingDataDetail.as_view()),

]