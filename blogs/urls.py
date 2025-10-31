from django.urls import path
from .views import homepage, blogpage, show_allpage, aboutpage

urlpatterns = [
    path('', homepage,),
    path('blog/', blogpage,),
    path('show_all/', show_allpage,),
    path('about/', aboutpage,),
]