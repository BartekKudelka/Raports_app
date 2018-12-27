from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=30)
    NIP_number = models.CharField(max_length=30)

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


class User(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    login = models.CharField(max_length=20)

    def login(self):
        return

    def logout(self):
        return

    def register(self):
        return


class Report(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def addReport(self):
        return

    def editReport(self):
        return

    def deleteReport(self):
        return

    def getReport(self):
        return

    def generateChart(self):
        return

    def generateTable(self):
        return


class Invoice(models.Model):
    client = models.ForeignKey(Client)
    date_of_issue = models.DateField()
    reports = models.ManyToManyField(Report, null=True)


class InvoiceItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    purchase_value = models.FloatField()
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)

    def addPurchase(self):
        return

    def deletePurchase(self):
        return
