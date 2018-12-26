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
    client_id = models.IntegerField(null=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    phone_nr = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    company_id = models.IntegerField(null=True)

    def addClient(self):
        return

    def deleteClient(self):
        return

    def changeData(self):
        return

class Product(models.Model):
    product_id = models.IntegerField(null=True)
    name = models.CharField(max_length=100)
    price = models.FloatField(null=True)
    producer = models.CharField(max_length=100)


    def addProduct(self):

        return

    def deleteProduct(self):
        return

    def changeData(self):
        return


class Purchase(models.Model):
    purchase_id = models.IntegerField(null=True)
    product_id = models.IntegerField(null=True)
    quantity = models.IntegerField(null=True)
    purchase_value = models.FloatField(null=True)


    def addPurchase(self):
        return


    def deletePurchase(self):
        return

class Invoice(models.Model):
    invoice_id = models.IntegerField(null=True)


class User(models.Model):
    user_id = models.IntegerField(null=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length = 50)
    password = models.CharField(max_length=20)

    def addUser(self):
        return

    def deleteUser(self):
        return