from django.urls import path
from . import views

urlpatterns=[

    path('',views.user_login,name='login'),

    path('dashboard/',views.dashboard,name='dashboard'),

    path('logout/',views.user_logout,name='logout'),

    path('leave/',views.leave_apply,name='leave'),
]