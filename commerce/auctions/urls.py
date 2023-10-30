from django.urls import path

from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("food", views.food, name="food"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("", views.home, name="home"),
    path("index", views.index, name="index"),
    path("Bookings", views.Booking, name="booking"),
    path("train", views.train, name="train"),
    path("<int:listing_id>/order", views.order, name="order"),
    path("<int:listing_id>/display_food", views.display_food, name="display_food"),
    path("<int:listing_id>/train_booking", views.book, name="train_booking"),
]