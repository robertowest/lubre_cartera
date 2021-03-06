from django.urls import path
from apps.empresa import views

app_name = __package__.split('.')[1]

urlpatterns = [
    path('', views.EmpresaTemplateView.as_view(), name='index'),
    path('listado/', views.EmpresaListView.as_view(), name='list'),
    path('crear/', views.EmpresaCreateView.as_view(), name='create'),
    path('<int:pk>/', views.EmpresaDetailView.as_view(), name='detail'),
    path('<int:pk>/modificar/', views.EmpresaUpdateView.as_view(), name='update'),
    path('<int:pk>/eliminar/', views.EmpresaDeleteView.as_view(), name='delete'),
    # listado de empresas con filtro
    path('filtro_actividad/<int:filtro>', views.FilterListView.as_view(), name='filtro_actividad'),
    path('filtro_comercial/<int:filtro>', views.FilterListView.as_view(), name='filtro_comercial'),
    # alta de registros vinculados a la empresa
    path('<int:fk>/comunicacion/', views.CreateComunicationView.as_view(), name='associate_with_comunication'),
    path('<int:fk>/domicilio/', views.CreateAddressView.as_view(), name='associate_with_address'),
    path('<int:fk>/contacto/', views.CreateContactView.as_view(), name='associate_with_contact'),
    path('<int:fk>/actividad/', views.ActividadMultiListView.as_view(), name='associate_with_actividad'),
]
