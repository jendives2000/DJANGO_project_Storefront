from django.db import models


class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()


class Collection(models.Model):
    title = models.CharField(max_length=255)
    # 1toM relationship: parent Product BUT !!! as a Parent, Product SHOULD HAVE BEEN positioned before this, Collection class.
    # This is why it is written in "" as in "Product"
    featured_product = models.ForeignKey(
        "Product", on_delete=models.SET_NULL, null=True, related_name="+"
    )


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)
    # 1toMany relationship: parent Collection
    # one collection can have many products
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    # MtoM relationship: parent: Promotion
    # many promotions can have many products and vice versa
    promotions = models.ManyToManyField(Promotion, related_name="promoted_products")


class Customer(models.Model):
    MEMBERSHIP_BRONZE = "B"
    MEMBERSHIP_SILVER = "S"
    MEMBERSHIP_GOLD = "G"

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, "Bronze"),
        (MEMBERSHIP_SILVER, "Silver"),
        (MEMBERSHIP_GOLD, "Gold"),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(
        max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE
    )


class Order(models.Model):
    PAYMENT_PENDING = "P"
    PAYMENT_COMPLETE = "C"
    PAYMENT_FAILED = "F"

    PAYMENT_STATUSES_CHOICES = [
        (PAYMENT_PENDING, "Pending"),
        (PAYMENT_COMPLETE, "Complete"),
        (PAYMENT_FAILED, "Failed"),
    ]
    place_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, choices=PAYMENT_STATUSES_CHOICES, default=PAYMENT_PENDING
    )
    # 1toM relationship: parent: Customer
    # one customer can have many Orders
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    # 1toMany relationship: parent: Customer
    # 1 client to many addresses
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # 1to1 relationship: parent : Customer
    # customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)


class OrderItem(models.Model):
    # 1toM relationship: parent: Order
    # 1 order can have many OrderItems
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    # 1toM relationship: parent: product
    # 1 product can have many OrderItems
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    # unit_price is here to capture the price AT THE TIME the order is made
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    # 1toM relationship: parent: Cart
    # 1 cart can have many CartItem
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    # 1toM relationship: parent: product
    # 1 product can have many CartItem
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
