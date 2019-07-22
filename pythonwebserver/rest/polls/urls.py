from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'questions', views.QuestionViewSet)

app_name = 'polls'

urlpatterns = [

    # # /polls/

    # our own view
    # path('', views.index, name='index'),

    # Return a nice automatic rest service
    # path('', include(router.urls)),

    # Generic view
    path('', views.IndexView.as_view(), name='index'),

    # # ex: /polls/5/

    # Our own view
    # path('<int:question_id>/', views.detail, name='detail'),

    # Generic view
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    # # ex: /polls/5/results/

    # Our own view
    # path('<int:question_id>/results/', views.results, name='results'),

    # Generic view
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),

    # # ex: /polls/5/vote/

    # Our own view
    # path('<int:question_id>/vote/', views.vote, name='vote'),

    # Generic view
    path('<int:question_id>/vote/', views.vote, name='vote'),

    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
