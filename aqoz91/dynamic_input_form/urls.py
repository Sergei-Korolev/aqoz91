from django.urls import path
from . import views


# urlpatterns = [
#     path('', views.index, name='index'),
#     path('show_result/', views.detail, name='detail')
# ]

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/', views.detail, name='detail'),
    path('delete_item/<int:id>/', views.delete_item, name='delete_item')
]
