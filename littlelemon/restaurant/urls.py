#define URL route for index() view
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import include, path
from . import views

router: DefaultRouter = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    # show menuitems
    path('api/menu/', views.MenuItemsView.as_view()),
    path('api/menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api/book/', views.BookingView.as_view()),
    path('api/book/<int:pk>', views.SingleBookingView.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]