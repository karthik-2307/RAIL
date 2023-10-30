from django.contrib.auth.models import AbstractUser
from django.db import models
class User(AbstractUser):
    pass
class Food(models.Model):
    name=models.CharField(null=False,max_length=250)
    ingredients=models.CharField(null=False,max_length=250)
    desc=models.CharField(null=False,max_length=250)
    Non_veg=models.BooleanField(null=False)
    price=models.IntegerField(null=False)
    a_img=models.CharField(null=False,max_length=1000,default="Image 1 link")
    b_img=models.CharField(null=False,max_length=1000,default="Image 2 link")
    c_img=models.CharField(null=False,max_length=1000,default="Image 3 link")
    def __str__(self) -> str:
        return f"Food name-{self.name}: non-veg {self.Non_veg}"
class Train(models.Model):
    train_name=models.CharField(max_length=250)
    train_no=models.IntegerField()
    mon=models.BooleanField()
    tue=models.BooleanField()
    wed=models.BooleanField()
    thu=models.BooleanField()
    fri=models.BooleanField()
    sat=models.BooleanField()
    sun=models.BooleanField()
    starting=models.CharField(max_length=100,default="ABH")
    ending=models.CharField(max_length=100,default="ABH")
    route=models.CharField(max_length=1000)
    b_ac=models.IntegerField()
    b_gen=models.IntegerField()
    b_sit=models.IntegerField()
    seats_in_ac=models.IntegerField()
    seats_in_gen=models.IntegerField()
    seats_in_sit=models.IntegerField()
    def __str__(self) -> str:
        return f"Train no-{self.train_no}: train_name {self.train_name} seats in ac {(self.seats_in_ac)*self.b_ac} seats in general {(self.seats_in_gen)*self.b_gen} seats in siting {(self.seats_in_sit)*self.b_sit} "

class FoodBookings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    name=models.ForeignKey(Food,on_delete=models.CASCADE, related_name="item")
    order_by=models.CharField(null=False,max_length=250)
    phn=models.IntegerField()
    train_no=models.IntegerField()
    seat_no=models.IntegerField()
    station=models.CharField(null=False,max_length=250)
    count=models.IntegerField()
    # cash_on_delivery=models.BooleanField()
    journey_date=models.DateField()
    def __str__(self) -> str:
        return f"Order by-{self.order_by}: train_no {self.train_no} on {self.journey_date} "
class Bookings(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    train_no=models.ForeignKey(Train,on_delete=models.CASCADE,null=True)
    From=models.CharField(max_length=250)
    to=models.CharField(max_length=150)
    Date=models.DateField()
    Count=models.IntegerField()
    mobile=models.IntegerField()
    def __str__(self):
       return f"Booked by {self.user} from {self.From} to {self.to} journey on {self.Date} with {self.Count} of passengers "
    