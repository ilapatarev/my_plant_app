from django.urls import path

from my_plant_app.web import views

urlpatterns=[
    path('', views.index, name='index'),
    path('catalogue', views.catalogue, name='catalogue'),
    path('plant/create', views.create_plant, name='create-plant'),
    path('plant/details/<int:pk>', views.plant_details, name='plant-details'),
    path('plant/edit/<int:pk>', views.edit_plant, name='edit-plant'),
    path('plant/delete/<int:pk>', views.plant_delete, name='plant-delete'),
    path('profile/create', views.create_profile, name='create-profile'),
    path('profile/details', views.profile_details, name='profile-details'),
    path('profile/edit', views.edit_profile, name='edit-profile'),
    path('profile/delete', views.profile_delete, name='profile-delete'),

]