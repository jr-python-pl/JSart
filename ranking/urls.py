from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import RankingView
from django.utils.translation import ugettext_lazy as _

app_name = 'ranking'
urlpatterns = [
    path(_('ranking/'), RankingView.as_view(), name="ranking"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)