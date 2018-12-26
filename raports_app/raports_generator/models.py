from django.db import models

# Create your models here.
class Report(models.Model):
    report_id = models.IntegerField(null=True)
    invoice_id = models.IntegerField(null=True)
    date_of_generation = models.DateField(null=True)

    def getReport(self):
        return

    def generateChart(self):
        return

    def generateTable(self):
        return



class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    NIP_number = models.CharField(max_length=30)
    email = models.CharField(max_length=50)

    def addClient(self):
        return

    def deleteClient(self):
        return


class Product(models.Model):
    name = models.CharField(max_length=100)

    def addProduct(self):

        return

    def deleteProduct(self):
        return


class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True)
    purchase_value = models.FloatField(null=True)

    def addPurchase(self):
        return


    def deletePurchase(self):
        return


class Invoice(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete = models.CASCADE)


class User(models.Model):
    login = models.CharField(max_length=20)
    email = models.CharField(max_length = 50)
    password = models.CharField(max_length=20)

    def login(self):
        return

    def logout(self):
        return

    def register(self):
        return


class Report(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    invoice = models.ForeignKey(Invoice, on_delete = models.CASCADE)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    def addReport(self):
        return

    def editChart(self):
        return

    def deleteTable(self):
        return