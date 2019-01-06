from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=30)
    NIP_number = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Product(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Invoice(models.Model):
    client = models.ForeignKey(Client)
    date_of_issue = models.DateField()

    def __str__(self):
        return str(self.date_of_issue)


class Report(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    invoices = models.ManyToManyField(Invoice, related_name="reports")


class InvoiceItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    purchase_value = models.FloatField()
    invoice = models.ForeignKey(Invoice, related_name="invoice_item")

    def __str__(self):
        return str(self.product) + " " + str(self.quantity) + " szt " + str(self.purchase_value)
