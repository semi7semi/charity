from django.contrib.auth.models import User

from charity_app.models import Category, Institution, Donation

# CATEGORY_CHOICE = (
#     ("Ubrania"),
#     ("Zabawki"),
#     ("Ubranka dziecięce"),
#     ("Książki")
# )
#
# for cat in CATEGORY_CHOICE:
#     Category.objects.create(
#         name = cat
#     )
#
# I1 = Institution.objects.create(
#     name=f"Fundacja nr 1",
#     description=f"Krótki opis fundacji 1",
#     type="fundation",
# )
# c1 = Category.objects.get(pk=4)
# c2 = Category.objects.get(pk=2)
# c2 = Category.objects.get(pk=3)
# # I1.categories.add(c1)
# I1 = Institution.objects.get(pk=4)
# I1.categories.add(c1)
# I1.categories.add(c2)
# I1.categories.add(c2)
#
# I2 = Institution.objects.create(
#     name=f"Fundacja nr 2",
#     description=f"Krótki opis fundacji 2",
#     type="fundation",
# )
# c2 = Category.objects.get(pk=2)
# I2.categories.add(c2)
#
# I3 = Institution.objects.create(
#     name=f"Organizacja AAA",
#     description=f"Krótki opis organizacji pozarzadowej AAA",
#     type="organization",
# )
# o3 = Category.objects.get(pk=3)
# I3.categories.add(o3)
#
# I4 = Institution.objects.create(
#     name=f"Organizacja BBB",
#     description=f"Krótki opis organizacji pozarzadowej BBB",
#     type="organization",
# )
# o4 = Category.objects.get(pk=1)
# I4.categories.add(o4)
#
# I5 = Institution.objects.create(
#     name=f"Zbiórka lokalna książek",
#     description=f"Krótki opis lokalnej zboiórki książek na Woli",
#     type="local",
# )
# o5 = Category.objects.get(pk=4)
# I5.categories.add(o5)

c1 = Category.objects.get(pk=2)
c2 = Category.objects.get(pk=4)
D1 = Donation.objects.create(
    quantity = 4,
    institution = Institution.objects.get(pk=2),
    address = "adress 22",
    phone_number = "1230000000",
    city = "Warszawa",
    zip_code = "22-444",
    pick_up_date = "2021-01-10",
    pick_up_time = "20:00",
    pick_up_comment = "komentarz do zamowienia nr 2",
    user = User.objects.get(id=5)
)

D2 = Donation.objects.create(
    quantity = 1,
    institution = Institution.objects.get(pk=5),
    address = "adress 3",
    phone_number = "333444555",
    city = "Warszawa",
    zip_code = "55-255",
    pick_up_date = "2021-01-15",
    pick_up_time = "12:00",
    pick_up_comment = "komentarz do zamowienia nr 3",
    user = User.objects.get(id=5)
)
D1.categories.add(c1)
D2.categories.add(c2)

