#!/usr/bin/env python

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'test_dmp.settings'
import django
django.setup()

from chf import models as chfmod
from django.db import connection
import subprocess
import sys
from django.contrib.auth.models import Group, Permission
from datetime import datetime, timedelta

cursor = connection.cursor()
cursor.execute("DROP SCHEMA PUBLIC CASCADE")
cursor.execute("CREATE SCHEMA PUBLIC")
subprocess.call([sys.executable, "manage.py", "migrate"])

address1 = chfmod.Address()
address1.street1 = '2300 North State st.'
address1.city = 'Orem'
address1.state = 'UT'
address1.zip_code = '84606'
address1.save()

address2 = chfmod.Address()
address2.street1 = '788 East 750 North'
address2.city = 'Provo'
address2.state = 'UT'
address2.zip_code = '84606'
address2.save()

user = chfmod.User()
user.first_name = 'Admin'
user.last_name = 'Colson'
user.username = 'ccolson'
user.email = 'codymcolson@gmail.com'
user.set_password('password')
user.is_superuser = True
user.save()
print('User Cody Created')

user1 = chfmod.User()
user1.first_name = 'Manager'
user1.last_name = 'Wight'
user1.username = 'blake'
user1.email = 'mrcolson12@gmail.com'
user1.set_password('password')
user1.is_staff = True
user1.save()
print('User Blake Created')

user2 = chfmod.User()
user2.first_name = 'Plain User'
user2.last_name = 'Wise'
user2.username = 'jwise'
user2.email = 'cody.colson@mozenda.com'
user2.set_password('password')
user2.save()
print('User Jordan Created')

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

photo3 = chfmod.Photograph()
photo3.image = 'item/media/printing_press.jpg'
photo3.save()

cat1 = chfmod.Category()
cat1.name = 'Weapons'
cat1.save()

cat2 = chfmod.Category()
cat2.name = 'Decoration'
cat2.save()

cat3 = chfmod.Category()
cat3.name = 'Clothing'
cat3.save()

p1 = chfmod.ProductSpecification()
p1.name = 'Pistolette'
p1.price = 1000.00
p1.description = 'this is going to be a really long bit of text to see what my stupid wells look like when text wraps. Pretty stupid, I agree, but I was just curious to see what happens.'
p1.manufacturer = 'Smith & Wesson'
p1.category = chfmod.Category.objects.get(name='Weapons')
p1.sku = 123456789
p1.average_cost = 1000.00
p1.photo = chfmod.Photograph.objects.create(image="chf/media/pistol.jpg")
print('image #1:' + p1.photo.image)
p1.quantity_on_hand = 5
p1.shelf_location = 'somehwere'
p1.save()

p2 = chfmod.ProductSpecification()
p2.name = 'Old Flag'
p2.price = 100.50
p2.description = 'Just a flag'
p2.manufacturer = "'Merica"
p2.category = chfmod.Category.objects.get(name='Decoration')
p2.sku = 123456789
p2.average_cost = 100.00
p2.photo = chfmod.Photograph.objects.create(image="chf/media/old_flag.jpg")
print('image #2:' + p2.photo.image)
p2.quantity_on_hand = 1
p2.shelf_location = 'somehwere'
p2.save()

# prod = chfmod.RentalProduct()
# prod.name = "the thing"
# prod.price = 2.00
# prod.save()

# item = chfmod.RentalItem()
# item.date_due = '2014-3-6'
# item.rental_product= chfmod.RentalProduct.objects.get(id=prod.id)
# item.save()

event = chfmod.Event()
event.name = 'Colonial Heritage Festival'
event.description = 'Annual gathering of colonial heritage fans. Fun for all ages.'
event.start_date = '2015-04-20'
event.end_date = '2015-04-23'
event.map_file_name = 'CHF-2015.pdf'
event.venue_name = 'Scera Outdoor Park'
event.address = chfmod.Address.objects.get(id=address1.id)
event.save()

area = chfmod.Area()
area.name = 'Cow milking'
area.description = 'People will come and milk cows for enjoyment'
area.event = chfmod.Event.objects.get(id = event.id)
area.place_number = 1
area.save()

area = chfmod.Area()
area.name = 'Blacksmith'
area.description = 'Make a horseshoe to take home!'
area.event = chfmod.Event.objects.get(id = event.id)
area.place_number = 2
area.save()

area = chfmod.Area()
area.name = 'Civil war musket-shooting'
area.description = 'Shoot a gun, win a prize.'
area.event = chfmod.Event.objects.get(id = event.id)
area.place_number = 3
area.save()

eventItem = chfmod.ExpectedSaleItem()
eventItem.name = 'Cow milking bucket'
eventItem.description = "It's a bucket for milking cows, keep it forever as a memory to this epic day when you milked a cow with your bare hands."
eventItem.low_price = 2.00
eventItem.high_price = 10.00
eventItem.photo = ''
eventItem.event = chfmod.Event.objects.get(id = event.id)
eventItem.save()

eventItem = chfmod.ExpectedSaleItem()
eventItem.name = 'Horseshoe'
eventItem.description = "Buy some metal and forge your own shoe."
eventItem.low_price = 12.00
eventItem.high_price = 25.00
eventItem.photo = ''
eventItem.event = chfmod.Event.objects.get(id = event.id)
eventItem.save()

eventItem = chfmod.ExpectedSaleItem()
eventItem.name = 'Basket'
eventItem.description = "Get a basket made for you and your family. Customizable."
eventItem.low_price = 30.00
eventItem.high_price = 50.00
eventItem.photo = ''
eventItem.event = chfmod.Event.objects.get(id = event.id)
eventItem.save()

rental = chfmod.RentalProduct()
rental.name = 'Colonial Jacket thing'
rental.price = 500.00
rental.description = 'A jacket that people from a long time ago would wear around all of the time.'
rental.manufacturer = 'Colonial Outerwear'
rental.average_cost = 350.00
rental.sku = '23gK85hQT56'
rental.order_form_name = 'Colonial Custom Jacket Order Form'
rental.production_time = 'Takes like 1 month to make'
rental.category = chfmod.Category.objects.get(id=2)
rental.shelf_location = 'in the back'
rental.product_order_file = 'blah blah blah'
rental.serial_number = 'asdpfi136137qef'
rental.date_acquired = '2014-03-07'
rental.cost = rental.average_cost
rental.notes = 'this thing is a good thing'
rental.price_per_day = 5.00
rental.save()

rental2 = chfmod.RentalProduct()
rental2.name = 'Colonial Musket'
rental2.price = 1500.00
rental2.description = 'muzzle loader in the style of a colonial musket'
rental2.manufacturer = 'Colonial Collectables'
rental2.average_cost = 1500.00
rental2.sku = '23gK85hQT56-67rpV'
rental2.order_form_name = 'Musket Order Form'
rental2.production_time = '2.5 months on average'
rental2.category = chfmod.Category.objects.get(id=1)
rental2.shelf_location = 'In the locker'
rental2.product_order_file = 'blah blah blah'
rental2.serial_number = 'g1645Frif6137qef'
rental2.date_acquired = '2014-09-07'
rental2.cost = rental.average_cost
rental2.notes = 'can hit the broad side of a barn at 100 yards!'
rental2.price_per_day = 20.00
rental2.save()

transaction = chfmod.Transaction()
transaction.order_date = datetime.today()
transaction.customer = user
transaction.save()

rent = chfmod.RentalItem()
rent.rental_product = chfmod.RentalProduct.objects.get(id=rental.id)
rent.date_due = '2014-11-26 00:00:00'
rent.amount = rent.rental_product.price_per_day * 7
rent.date_in = None
rent.discount_percent = None
rent.transaction = transaction
rent.save()
rent.date_out = '2014-11-25 00:00:00'
rent.save()

rent2 = chfmod.RentalItem()
rent2.rental_product = chfmod.RentalProduct.objects.get(id=rental2.id)
rent2.date_due = '2014-11-26 00:00:00'
rent2.amount = rent.rental_product.price_per_day * 7
rent2.date_in = None
rent2.discount_percent = None
rent2.transaction = transaction
rent2.save()
rent2.date_out = '2014-11-25 00:00:00'
rent2.save()


transaction.save()

transaction = chfmod.Transaction()
transaction.order_date = '2015-01-02 00:00:00'
transaction.customer = user1
transaction.save()

rent = chfmod.RentalItem()
rent.rental_product = chfmod.RentalProduct.objects.get(id=rental.id)
rent.date_due = '2015-01-10 00:00:00'
rent.amount = rent.rental_product.price_per_day * 7
rent.date_in = None
rent.discount_percent = None
rent.transaction = transaction
rent.save()
rent.date_out = '2014-01-07 00:00:00'
rent.save()

rent2 = chfmod.RentalItem()
rent2.rental_product = chfmod.RentalProduct.objects.get(id=rental2.id)
rent2.date_due = '2015-01-10 00:00:00'
rent2.amount = rent.rental_product.price_per_day * 7
rent2.date_in = '2015-01-09 00:00:00'
rent2.discount_percent = None
rent2.transaction = transaction
rent2.save()
rent2.date_out = '2014-01-07 00:00:00'
rent2.save()

transaction.save()

transaction = chfmod.Transaction()
transaction.order_date = '2014-10-03 00:00:00'
transaction.customer = user
transaction.save()

rent = chfmod.RentalItem()
rent.rental_product = chfmod.RentalProduct.objects.get(id=rental.id)
rent.date_due = '2015-02-10 00:00:00'
rent.amount = rent.rental_product.price_per_day * 7
rent.date_in = None
rent.discount_percent = None
rent.transaction = transaction
rent.save()
rent.date_out = '2015-02-03 00:00:00'
rent.save()

rent2 = chfmod.RentalItem()
rent2.rental_product = chfmod.RentalProduct.objects.get(id=rental2.id)
rent2.date_due = '2015-02-10 00:00:00'
rent2.amount = rent.rental_product.price_per_day * 7
rent2.date_in = None
rent2.discount_percent = None
rent2.transaction = transaction
rent2.save()
rent2.date_out = '2015-02-03 00:00:00'
rent2.save()


transaction.save()
