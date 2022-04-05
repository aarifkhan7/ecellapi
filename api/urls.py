from django.urls import path

from . import views
urlpatterns=[
  path('create-event/', views.createevent),
  path('fetch-events/', views.printevents),
  path('fetch-events/<int:year>', views.printeventsbyyear),
  path('delete-event/<int:id>', views.deletevent),
]