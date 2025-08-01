from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from paginas import views as paginas_views

urlpatterns = [
    # painel admin
    path('admin/', admin.site.urls),
    
    # principais seções do parque
    path('', include('atracoes.urls', namespace='atracoes')),
    path('eventos/', include('eventos.urls', namespace='eventos')),
    path('restaurantes/', include('restaurantes.urls', namespace='restaurantes')),
    path('hoteis/', include('hoteis.urls', namespace='hoteis')),
    path('ingressos/', include('ingressos.urls', namespace='ingressos')),
    path('usuarios/', include('usuarios.urls', namespace='usuarios')),
    path('servicos/', include('servicos.urls', namespace='servicos')),
    
    # páginas institucionais
    path('sobre-nos/', paginas_views.sobre_nos, name='sobre_nos'),
    path('termos-de-uso/', paginas_views.termos_uso, name='termos_uso'),
    path('politica-de-privacidade/', paginas_views.politica_privacidade, name='politica_privacidade'),
    path('faq/', paginas_views.faq, name='faq'),
    
    # favicon
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico', permanent=True)),
]

# serve arquivos estáticos em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# personaliza o admin
admin.site.site_header = "Infinity Park - Administração"
admin.site.site_title = "Infinity Park Admin"
admin.site.index_title = "Painel de Controle do Infinity Park"