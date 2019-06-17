from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import RankingView

app_name = 'ranking'
urlpatterns = [
    path('ranking/', RankingView.as_view(), name="ranking"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)