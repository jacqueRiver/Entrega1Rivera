from django.urls import path
from proyectocoder.Pentrega.views import PentregaView, SearchView
from django.views.generic import TemplateView


app_name = "v2"
urlpatterns = [
    path('', TemplateView.as_view(template_name="v2/index.html"), name='v2'),
    path('pentrega/', PentregaView.as_view(), name='pentregav2'),
    
    path('search/', SearchView.as_view(), name='search')



]

