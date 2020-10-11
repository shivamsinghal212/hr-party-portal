from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import User
from django.db import models
from smart_selects.db_fields import ChainedForeignKey


# Create your models here.

class Base(models.Model):
    ANDROID = 1
    WEB = 2
    IOS = 3
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    platform = models.PositiveSmallIntegerField(null=True)
    soft_delete = models.PositiveSmallIntegerField(default=0)

    class Meta:
        abstract = True


class Party(Base):
    ACTIVE = 1
    INACTIVE = 0
    name = models.CharField(max_length=50, unique=True, null=False, blank=False)
    status = models.SmallIntegerField(default=ACTIVE, choices=[(0, 'INACTIVE'), (1, 'ACTIVE')])

    class Meta:
        verbose_name_plural = "Parties"

    def __str__(self):
        return self.name


class MenuItems(Base):
    ADDED = 1
    DELETED = 0
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    status = models.SmallIntegerField(default=ADDED)
    description = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        verbose_name_plural = "Party items"
        unique_together = ["party", "description"]

    def __str__(self):
        return f"{self.description}"


class NewOrder(models.Model):
    OPEN = 1
    CLOSED = 0
    employee = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    party = models.ForeignKey(Party, on_delete=models.CASCADE, null=False)
    item = ChainedForeignKey(
        MenuItems,
        chained_field="party",
        chained_model_field="party",
        show_all=False,
        auto_choose=True,
        sort=True)
    status = models.SmallIntegerField(default=OPEN, choices=[(1, 'OPEN'), (0, 'CLOSED')])
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name_plural = "New Orders"

    def __str__(self):
        return f"{self.party.name}"

# class Orders(Base):
#     OPEN = 1
#     CLOSED = 0
#     employee = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
#     party = models.ForeignKey(Party, on_delete=models.CASCADE, null=False)
#     status = models.SmallIntegerField(default=OPEN, choices=[(1, 'OPEN'), (0, 'CLOSED')])
#
#     class Meta:
#         verbose_name_plural = "Orders"
#         unique_together = ["employee", "party"]
#
#     def __str__(self):
#         return f"{self.party.name}"
#
#
# class OrderItems(Base):
#     # party = models.ForeignKey(Party, on_delete=models.CASCADE, null=False)
#     order = models.ForeignKey(Orders, on_delete=models.CASCADE)
#     item = ChainedForeignKey(
#             MenuItems,
#             chained_field="order",
#             chained_model_field="party",
#             show_all=False,
#             auto_choose=True,
#             sort=True)
#
#     class Meta:
#         verbose_name_plural = "Order Items"
#         unique_together = ["order", "item"]
#
#     def __str__(self):
#         return f"{self.item.description}"
