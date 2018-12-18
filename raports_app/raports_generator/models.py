from django.db import models

# Create your models here.
class Report(models.Model):
    id_report = models.IntegerField(null=True)
    id_invoice = models.IntegerField(null=True)
    data_wygenerowania = models.DateField(null=True)

    def getReport(self):
        return

    def generateChart(self):
        return

    def generateTable(self):
        return



class Client (models.Model):
    id_client = models.IntegerField(null=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    phone_nr = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    id_company = models.IntegerField(null=True)

    def addClienta(self):
        return

    def deleteKlienta(self):
        return

    def changeData(self):
        return

class Product (models.Model):
    id_product = models.IntegerField(null=True)
    name = models.CharField(max_length=100)
    price = models.FloatField(null=True)
    producer = models.CharField(max_length=100)


    def addProduct(self):

        return

    def deleteProduct(self):
        return

    def changeData(self):
        return


class Purchase (models.Model):
    id_purchase = models.IntegerField(null=True)
    id_product = models.IntegerField(null=True)
    quantity = models.IntegerField(null=True)
    purchase_value = models.FloatField(null=True)


    def addPurchase(self):
        return


    def deletePurchase(self):

        return