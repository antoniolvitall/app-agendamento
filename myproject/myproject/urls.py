from agendamento.views import ConsultaViewSet, ProfissionalViewSet
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

urlpatterns = [
    path('admin/', admin.site.urls),x
]


router = routers.DefaultRouter()
router.register('profissionais', ProfissionalViewSet)
router.register('consultas', ConsultaViewSet)


