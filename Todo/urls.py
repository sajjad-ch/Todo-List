from django.urls import path, include
from Todo.views import TodosGenericApiView, TodosGenericDetailView

urlpatterns = [
    path('todo/', TodosGenericApiView.as_view()),
    path('todo/<pk>', TodosGenericDetailView.as_view()),
]
