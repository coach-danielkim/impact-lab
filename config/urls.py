from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('apps.home.urls')),
    path('education/', include('apps.education.urls')),
    path('admissions/', include('apps.admissions.urls')),
    path('ai-lab/', include('apps.ai_lab.urls')),
    path('veritas/', include('apps.veritas.urls')),
    path('contact/', include('apps.contact.urls')),
    path('blog/', include('apps.blog.urls')),
    path('events/', include('apps.events.urls')),
    path('faq/', include('apps.faq.urls')),
    path('newsletter/', include('apps.newsletter.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
