from django.contrib import admin 
from django.urls import path,include 
from django.conf import settings
from django.conf.urls.static import static 


urlpatterns = [
    path('',include('core.urls')),
    path('items/',include("item.urls")),
    path('admin/', admin.site.urls)
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# pentru a lucra cu informatia statica in django e nevoie de importat setarile 
# proiectului si functia in care se transmit parametrii in care la randul lor se pastreaza
# caile unde se afla fisierle statice 