from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("listings/<int:pk>/", views.LotDetailView.as_view(), name='lot_detail'),
    path("create_listing/", views.CreateListingView.as_view(), name="create_listing"),
    path("<int:pk>/listings/", views.UserListingsView.as_view(), name="user_listings"),
    path("<int:pk>/update_lot", views.LotUpdateView.as_view(), name="update_lot"),
    path("<int:pk>/delete_lot", views.LotDeleteView.as_view(), name="delete_lot"),
    path("<int:pk>/place_bid/", views.place_bid, name="place_bid"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)