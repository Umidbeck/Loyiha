from django.urls import path
from .views import AboutPageViews, AsdViews, BaseVieews, HomePageViews


urlpatterns = [
    path('', HomePageViews.as_view(), name="home"),
    path('about/',AboutPageViews.as_view(), name='about'),
    path('base/',BaseVieews.as_view(), name='base'),
    path('asd/',AsdViews.as_view, name='asd'),
]
