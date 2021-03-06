"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('comunicacion/', include('apps.comunes.urls.comunicacion')),
    path('diccionario/', include('apps.comunes.urls.diccionario')),
    path('domicilio/', include('apps.comunes.urls.domicilio')),

    path('empresa/', include('apps.empresa.urls.empresa')),
    path('empresa/actividad/', include('apps.empresa.urls.actividad')),

    path('persona/', include('apps.persona.urls')),
]


# Dashboard
from django.views.generic import TemplateView
urlpatterns += [
    # path('', TemplateView.as_view(template_name='dashboard.html'))
    path('', TemplateView.as_view(template_name='base.html'))
]


# DEBUG
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
