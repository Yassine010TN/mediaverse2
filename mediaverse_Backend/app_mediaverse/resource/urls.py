"""
URL mappings for the resource app.
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from resource import views


router1 = DefaultRouter()
router1.register('resources', views.ResourceViewSet, basename='resources')
router1.register('categories', views.CategoryViewSet, basename='categories')
router1.register('types', views.TypeViewSet, basename='types')
router1.register('all-resources', views.AllResourcesViewSet, basename='all-resources')
router1.register('all-categories', views.AllCategoriesViewSet, basename='all-categories')
router1.register('all-types', views.AllTypesViewSet, basename='all-types')

app_name = 'resource'

urlpatterns = [
    path('', include(router1.urls)),
]