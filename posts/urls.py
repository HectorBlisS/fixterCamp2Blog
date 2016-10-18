from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$',
		views.Hola.as_view(),
		name="home"),

	url(r'^blog/$',
		views.Listado.as_view(),
		name="lista"),
]