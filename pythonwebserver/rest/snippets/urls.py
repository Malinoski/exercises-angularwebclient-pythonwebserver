from django.urls import path
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    # # Function based views:
    # path('snippets/', views.snippet_list),
    # path('snippets/<int:pk>/', views.snippet_detail),

    # # Class based views
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),

    # # Include login/logout page
    path('api-auth/', include('rest_framework.urls'))
]

# This allow to add the response format, used in functions (snippet_list) or classes (SnippetDetail, SnippetList))
urlpatterns = format_suffix_patterns(urlpatterns)

