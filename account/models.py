from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=13)
    avatar = models.ImageField(upload_to='avatar/')

    def __str__(self):
        return self.username


class Balance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    ball = models.IntegerField(default=0)
    account_id = models.CharField(max_length=32, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.account_id = f"A{self.id}{self.user.id}"
        super(Balance, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username}"