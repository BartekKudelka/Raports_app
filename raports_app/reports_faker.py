import os, django, random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "raports_app.settings")
django.setup()

from raports_generator.models import Client, InvoiceItem, Product, Report, Invoice, User
from faker import Faker

fakegen = Faker('pl_PL')


def add_invoice_item():
    i = InvoiceItem.objects.get_or_create()[0]
    i.save()
    return i


def add_user():
    u = User.objects.get_or_create(password='zaq1@WSX', email=fakegen.name())[0]
    u.save()
    return u


def add_product():
    p = Product.objects.get_or_create(
        name=fakegen.name()
    )[0]
    p.save()
    return p

def add_client():
    c = Client.objects.get_or_create(
        first_name = fakegen.first_name(),
        last_name = fakegen.last_name(),
        phone_number = fakegen.phone_number(),
        NIP_number = fakegen.phone_number(),
        email = fakegen.email()
    )[0]
    c.save()
    return c

def populate(N=20):
    fake_id = random.randint(1, 6)
    fake_email = fakegen.email()
    fake_number = fakegen.phone_number()
    # fake_firstname = fakegen.first_name()
    # fake_secondname = fakegen.second_name()
    fake_ilosc = random.randint(1, 3)
    fake_kwotazakupu = random.randint(1, 4)
    fake_kwotawystawienia = random.randint(1, 4)

    fake_Nazwa = fakegen.text()
    fake_cena = random.randint(1, 2)
    fake_producent = fakegen.name

    for entry in range(N):
        #product = add_product()

        #user = add_user()

        client = add_client()

# client = Client.objects.get_or_create(client_id=fake_id, first_name=fake_firstname, last_name=fake_secondname, phone_number=fake_number, email=fakegen.email(), id_firmy=fake_id)[0]

# purchase = Purchase.objects.get_or_create(purchase_id=fake_id, id_produktu=fake_id, ilosc=fake_ilosc, kwotazakupu=fake_cena)[0]

# invoice = Invoice.objects.get_or_create(invoice_id=fake_id[0])

# product = Product.objects.get_or_create(id_produktu= fake_id, nazwa=fake_Nazwa, cena = fake_cena, producent=fake_producent)[0]

# report = Report.objects.get_or_create(id_raportu= fake_id, id_faktury=fake_id, datawygnereowania=fake_datawygenerowania)[0]

if __name__ == '__main__':
    print("populating data")
    populate(20)
    print("populating complete")
