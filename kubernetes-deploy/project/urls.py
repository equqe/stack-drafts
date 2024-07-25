from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path


def index(request):
    return HttpResponse('''
    <html>
        <head>
            <title>Demo</title>
        </head>
        <body>
            <h1>Demo</h1>
        </body>
    </html>
    ''')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)