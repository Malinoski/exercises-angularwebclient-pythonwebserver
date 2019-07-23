from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

"""
# API endpoints v1
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

"""
# API endpoints v2
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
"""

"""
# API endpoints v3

snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = format_suffix_patterns([

    # # Function based views:
    path('', api_root),

    # # Class based views:,
    path('snippets/', snippet_list, name='snippet-list'),
    path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail'),

    # # Include login/logout top fragment page
    path('api-auth/', include('rest_framework.urls'))
])
"""

# API endpoints v4

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),

    # # Include login/logout top fragment page
    path('api-auth/', include('rest_framework.urls'))
]