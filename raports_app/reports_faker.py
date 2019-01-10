import os, django, random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "raports_app.settings")
django.setup()

from django.contrib.auth.models import User
from raports_generator.models import Client, InvoiceItem, Product, Report, Invoice
from faker import Faker

fakegen = Faker('pl_PL')


def add_admin_user():
    password = 'zaq1@WSX'
    my_admin = User.objects.create_superuser('admin2', 'myemail@test.com', password)


def add_report():
    r = Report.objects.get_or_create(
        start_date=fakegen.date_between(start_date="-1y", end_date="today"),
        end_date=fakegen.date_between(start_date="-1y", end_date="today")
    )[0]
    r.save()
    return r


def add_invoice(client):
    i = Invoice.objects.get_or_create(
        client=client,
        date_of_issue=fakegen.date_between(start_date="-1y", end_date="today")
    )[0]
    i.save()
    return i


def add_invoice_item(product, invoice):
    i = InvoiceItem.objects.get_or_create(
        product=product,
        quantity=fakegen.random.randint(1, 25),
        purchase_value=fakegen.random.randint(1, 500),
        invoice=invoice
    )[0]
    i.save()
    return i


def add_product(index):
    products = [
        'sugar', 'eggs', 'yoghurt', 'margarine', 'butter', 'flour', 'milk', 'oil', 'baking powder', 'rice',
        'cheese', 'mild cheese', 'full fat cheese', 'cream cheese', 'cream', 'fat', 'egg yolk', 'sparkling',
        'mineral water', 'drink', 'chips', 'broth', 'soup', 'scrambled eggs', 'boiled eggs', 'fried eggs',
        'sausage', 'apple', 'pear', 'peach', 'omelette', 'brad', 'croissant', 'roll', 'donut', 'oats', 'groats',
        'pasta', 'perogies', 'noodles', 'olive oil', 'pork', 'beef', 'veal', 'lamb', 'rabbit', 'chicken', 'duck',
        'liver', 'turkey'
    ]
    p = Product.objects.get_or_create(name=products[index])[0]
    p.save()

    return p


def add_client():
    c = Client.objects.get_or_create(
        first_name=fakegen.first_name(),
        last_name=fakegen.last_name(),
        phone_number=fakegen.phone_number(),
        NIP_number=fakegen.phone_number(),
        email=fakegen.email()
    )[0]
    c.save()
    return c

def populate(N=50):
    index = 0

    products = [
        'sugar', 'eggs', 'yoghurt', 'margarine', 'butter', 'flour', 'milk', 'oil', 'baking powder', 'rice',
        'cheese', 'mild cheese', 'full fat cheese', 'cream cheese', 'cream', 'fat', 'egg yolk', 'sparkling',
        'mineral water', 'drink', 'chips', 'broth', 'soup', 'scrambled eggs', 'boiled eggs', 'fried eggs',
        'sausage', 'apple', 'pear', 'peach', 'omelette', 'brad', 'croissant', 'roll', 'donut', 'oats', 'groats',
        'pasta', 'perogies', 'noodles', 'olive oil', 'pork', 'beef', 'veal', 'lamb', 'rabbit', 'chicken', 'duck',
        'liver', 'turkey'
    ]

    for entry in range(N):
        product = add_product(index)
        client = add_client()
        report = add_report()

        invoice = add_invoice(client)

        for n in range(3):
            report.invoices.add(invoice)
            invoiceItem = add_invoice_item(products[n], invoice)

        index += 1
    report.invoices.add(invoice)


if __name__ == '__main__':
    print("populating data")
    populate(20)
    add_admin_user()
print("populating complete")