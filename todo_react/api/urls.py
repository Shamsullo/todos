from django.urls import path
from . import views

from django.urls import path
from api.views import(
	registration_view,
	ObtainAuthTokenView,
	account_properties_view,
	update_account_view,
	does_account_exist_view,
	ChangePasswordView,
)

urlpatterns =[
    path('', views.apiOverview, name='api-overview'),
    path('task-list/', views.taskList, name='task-list'),
    path('task-detail/<str:pk>/', views.taskDetail, name='task-detail'),
    path('task-create/', views.taskCreate, name='task-create'),
    path('task-update/<str:pk>/', views.taskUpdate, name='task-update'),
    path('task-delete/<str:pk>/', views.taskDelete, name='task-delete'),

    # registration and auth endpoints
    path('check_if_account_exists/', does_account_exist_view, name="check_if_account_exists"),
	path('change-password/', ChangePasswordView.as_view(), name="change_password"),
	path('properties/', account_properties_view, name="properties"),
	path('properties-update/', update_account_view, name="update"),
 	path('login/', ObtainAuthTokenView.as_view(), name="login"), 
	path('register/', registration_view, name="register"),
]