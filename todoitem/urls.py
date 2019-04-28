from django.conf.urls import url

from todoitem.views import TodoList, TodoDetail

urlpatterns = [
    url('^todolist/$', TodoList.as_view()),
    url('^todolist/(?P<task_name>[\w]+$)', TodoDetail.as_view()),
]
