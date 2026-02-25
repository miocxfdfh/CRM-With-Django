from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('register/',views.register, name='register'),
    path('login/',views.my_login, name='login'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('logout/',views.my_logout, name='logout'),
    path('create_record/',views.create_record, name='create_record'),
    path('view/<int:record_id>/',views.view_record, name='view'),
    path('update/<int:record_id>/',views.update_record, name='update'),
    path('delete/<int:record_id>/',views.delete_record, name='delete'),
    path('search/',views.search, name='search'),
]