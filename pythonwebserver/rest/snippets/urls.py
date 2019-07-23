from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    # # Function based views:
    # path('snippets/', views.snippet_list),
    # path('snippets/<int:pk>/', views.snippet_detail),

    # # Class based views
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]

# This allow to add the format parameter to functions (ex.: def snippet_list(request, format=None):)
urlpatterns = format_suffix_patterns(urlpatterns)

