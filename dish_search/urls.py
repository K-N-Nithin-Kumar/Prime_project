from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search_app/', include("search_app.urls")),
]
#dish_search\Resources\restaurants_small.csv