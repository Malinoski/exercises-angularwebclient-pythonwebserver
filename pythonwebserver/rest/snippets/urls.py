from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
]

# This allow to add the format parameter to functions (ex.: def snippet_list(request, format=None):)
urlpatterns = format_suffix_patterns(urlpatterns)
