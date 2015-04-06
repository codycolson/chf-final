#!/usr/bin/env python

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'chf.settings'
import django
django.setup()

import chf.models as chfmod
from django.db import connection
import subprocess
import sys

cursor = connection.cursor()
cursor.execute("DROP SCHEMA PUBLIC CASCADE")
cursor.execute("CREATE SCHEMA PUBLIC")
subprocess.call([sys.executable, "manage.py", "migrate"])

add = chfmod.Address()
add.street = '213 Main'
add.city = 'Provo'
add.state = 'UT'
add.zip_code = '84606'
add.save()

user = chfmod.User()
user.first_name = "Cody"
user.last_name = "Colson"
user.username = "cody"
user.email = "cody@gmail.com"
user.set_password("password")
user.is_superuser = False
user.is_staff = False
user.is_active = True
user.address = chfmod.Address.objects.get(id=1)
user.save()

user = chfmod.User()
user.first_name = "Mike"
user.last_name = "Tyson"
user.username = "mike"
user.email = "mike@gmail.com"
user.set_password("password")
user.is_superuser = False
user.is_staff = False
user.is_active = True
user.save()

cat = chfmod.Category()
cat.name = "Hats"
cat.save()

cat = chfmod.Category()
cat.name = "Pants"
cat.save()

cat = chfmod.Category()
cat.name = "Shirts"
cat.save()

cat = chfmod.Category()
cat.name = "Uniforms"
cat.save()

cat = chfmod.Category()
cat.name = "Guns"
cat.save()

photo = chfmod.Photograph()
photo.image = "chf/media/oldhat.jpg"
photo.save()

photo = chfmod.Photograph()
photo.image = "chf/media/oldpants.jpg"
photo.save()

photo = chfmod.Photograph()
photo.image = "chf/media/uniform.jpg"
photo.save()

photo = chfmod.Photograph()
photo.image = "chf/media/blueuniform.jpg"
photo.save()

photo = chfmod.Photograph()
photo.image = "chf/media/rifle.jpg"
photo.save()

prod = chfmod.RentalProduct()
prod.name = "this hat"
prod.description = "Do you see how nice it is?"
prod.manufacturer = "CHF"
prod.average_cost = 20
prod.price = 30
prod.category = chfmod.Category.objects.get(id=1)
prod.sku = 1234567890
prod.photo = chfmod.Photograph.objects.get(id=1)
prod.quantity_on_hand = 5
prod.cost = 35
prod.notes = "I hate this hat"
prod.times_rented = 4
prod.price_per_day = 5
prod.save()

prod = chfmod.RentalProduct()
prod.name = "ragged pants"
prod.description = "You do not want these pants."
prod.manufacturer = "CHF"
prod.average_cost = 50
prod.price = 70
prod.category = chfmod.Category.objects.get(id=2)
prod.sku = 123456789
prod.photo = chfmod.Photograph.objects.get(id=2)
prod.quantity_on_hand = 1
prod.cost = 35
prod.notes = "I hate these pants"
prod.times_rented = 4
prod.price_per_day = 5
prod.save()

tran = chfmod.Transaction()
tran.phone = '8307127364'
tran.ships_to = chfmod.Address.objects.get(id=1)
tran.customer = chfmod.User.objects.get(id=1)
tran.save()

prod = chfmod.RentalItem()
prod.transaction = chfmod.Transaction.objects.get(id=1)
prod.amount = 5
prod.date_due = '2015-03-25 00:00:00'
prod.discount_percent = '.5'
prod.rental_product = chfmod.RentalProduct.objects.get(id=1)
prod.save()

prod = chfmod.RentalItem()
prod.transaction = chfmod.Transaction.objects.get(id=1)
prod.amount = 7
prod.date_due = '2015-03-15 00:00:00'
prod.discount_percent = '.5'
prod.rental_product = chfmod.RentalProduct.objects.get(id=1)
prod.save()

prod = chfmod.RentalItem()
prod.transaction = chfmod.Transaction.objects.get(id=1)
prod.amount = 10
prod.date_due = '2015-03-15 00:00:00'
prod.discount_percent = '.5'
prod.rental_product = chfmod.RentalProduct.objects.get(id=2)
prod.save()

prod = chfmod.ProductSpecification()
prod.name = "Uniform that was actually worn"
prod.description = "It hasn't been washed."
prod.manufacturer = "CHF"
prod.average_cost = 50
prod.price = 120
prod.category = chfmod.Category.objects.get(id=4)
prod.sku = 12345678
prod.photo = chfmod.Photograph.objects.get(id=3)
prod.quantity_on_hand = 1
prod.save()

prod = chfmod.ProductSpecification()
prod.name = "Blue uniform"
prod.description = "Very handsome"
prod.manufacturer = "CHF"
prod.average_cost = 50
prod.price = 150
prod.category = chfmod.Category.objects.get(id=4)
prod.sku = 1234567
prod.photo = chfmod.Photograph.objects.get(id=4)
prod.quantity_on_hand = 1
prod.save()

prod = chfmod.ProductSpecification()
prod.name = "Rifle"
prod.description = "This is a dangerous gun. Do not fire."
prod.manufacturer = "Smith & Wesson"
prod.average_cost = 200
prod.price = 499
prod.category = chfmod.Category.objects.get(id=5)
prod.sku = 123456
prod.photo = chfmod.Photograph.objects.get(id=5)
prod.quantity_on_hand = 5
prod.save()
