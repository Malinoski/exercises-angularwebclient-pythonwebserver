from django.urls import path
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

# API endpoints


"""
urlpatterns = [
    # # Function based views:
    # path('snippets/', views.snippet_list),
    # path('snippets/<int:pk>/', views.snippet_detail),
    path('', views.api_root),

    # # Class based views 
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),

    # # Include login/logout page
    path('api-auth/', include('rest_framework.urls'))
]
# This allow to add the response format, used in functions (snippet_list) or classes (SnippetDetail, SnippetList))
urlpatterns = format_suffix_patterns(urlpatterns)
"""

urlpatterns = format_suffix_patterns([

    # # Function based views:
    path('', views.api_root),

    # # Class based views:,
    path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),

    # # Include login/logout top fragment page
    path('api-auth/', include('rest_framework.urls'))
])
