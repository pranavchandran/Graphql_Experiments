from graphene_django.views import GraphQLView
from django.contrib import admin
from django.urls import path, include
from .schema import schema
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('snippets/', include('snippets.urls', namespace='snippets')),
    path('graphql/', csrf_exempt(GraphQLView.as_view(
        graphiql=True,
        schema=schema))),
    path('admin/', admin.site.urls),
]
