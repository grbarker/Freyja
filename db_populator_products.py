from app import db
from app.models import Category, Supplier, Product



supplier = Supplier.query.get(int(1))
category = Category.query.get(int(1))
p1 = Product(productname="Chais", supplier=supplier, category=category, unit="10 boxes x 20 bags", price=18)
db.session.add(p1)

supplier = Supplier.query.get(int(1))
category = Category.query.get(int(1))
p2 = Product(productname="Chang", supplier=supplier, category=category, unit="24 - 12 oz bottles", price=19)
db.session.add(p2)

supplier = Supplier.query.get(int(1))
category = Category.query.get(int(2))
p3 = Product(productname="Aniseed Syrup", supplier=supplier, category=category, unit="12 - 55S0 ml bottles", price=10)
db.session.add(p3)

supplier = Supplier.query.get(int(2))
category = Category.query.get(int(2))
p4 = Product(productname="Chef Anton's Cajun Seasoning", supplier=supplier, category=category, unit="48 - 6 oz jars", price=22)
db.session.add(p4)

supplier = Supplier.query.get(int(2))
category = Category.query.get(int(2))
p5 = Product(productname="Chef Anton's Gumbo Mix", supplier=supplier, category=category, unit="36 boxes", price=21.35)
db.session.add(p5)

supplier = Supplier.query.get(int(3))
category = Category.query.get(int(2))
p6 = Product(productname="Grandma's Boysenberry Spread", supplier=supplier, category=category, unit="12 - 8 oz jars", price=25)
db.session.add(p6)

supplier = Supplier.query.get(int(3))
category = Category.query.get(int(7))
p7 = Product(productname="Uncle Bob's Organic Dried Pears", supplier=supplier, category=category, unit="12 - 1 lb pkgs.", price=30)
db.session.add(p7)

supplier = Supplier.query.get(int(3))
category = Category.query.get(int(2))
p8 = Product(productname="Northwoods Cranberry Sauce", supplier=supplier, category=category, unit="12 - 12 oz jars", price=40)
db.session.add(p8)

supplier = Supplier.query.get(int(4))
category = Category.query.get(int(6))
p9 = Product(productname="Mishi Kobe Niku", supplier=supplier, category=category, unit="18 - 500 g pkgs.", price=97)
db.session.add(p9)

supplier = Supplier.query.get(int(4))
category = Category.query.get(int(8))
p10 = Product(productname="Ikura", supplier=supplier, category=category, unit="12 - 200 ml jars", price=31)
db.session.add(p10)

supplier = Supplier.query.get(int(5))
category = Category.query.get(int(4))
p11 = Product(productname="Queso Cabrales", supplier=supplier, category=category, unit="1 kg pkg.", price=21)
db.session.add(p11)

supplier = Supplier.query.get(int(5))
category = Category.query.get(int(4))
p12 = Product(productname="Queso Manchego La Pastora", supplier=supplier, category=category, unit="10 - 500 g pkgs.", price=38)
db.session.add(p12)

supplier = Supplier.query.get(int(6))
category = Category.query.get(int(8))
p13 = Product(productname="Konbu", supplier=supplier, category=category, unit="2 kg box", price=6)
db.session.add(p13)

supplier = Supplier.query.get(int(6))
category = Category.query.get(int(7))
p14 = Product(productname="Tofu", supplier=supplier, category=category, unit="40 - 100 g pkgs.", price=23.25)
db.session.add(p14)

supplier = Supplier.query.get(int(6))
category = Category.query.get(int(2))
p15 = Product(productname="Genen Shouyu", supplier=supplier, category=category, unit="24 - 250 ml bottles", price=15.5)
db.session.add(p15)

supplier = Supplier.query.get(int(7))
category = Category.query.get(int(3))
p16 = Product(productname="Pavlova", supplier=supplier, category=category, unit="32 - 500 g boxes", price=17.45)
db.session.add(p16)

supplier = Supplier.query.get(int(7))
category = Category.query.get(int(6))
p17 = Product(productname="Alice Mutton", supplier=supplier, category=category, unit="20 - 1 kg tins", price=39)
db.session.add(p17)

supplier = Supplier.query.get(int(7))
category = Category.query.get(int(8))
p18 = Product(productname="Carnarvon Tigers", supplier=supplier, category=category, unit="16 kg pkg.", price=62.5)
db.session.add(p18)

supplier = Supplier.query.get(int(8))
category = Category.query.get(int(3))
p19 = Product(productname="Teatime Chocolate Biscuits", supplier=supplier, category=category, unit="10 boxes x 12 pieces", price=9.2)
db.session.add(p19)

supplier = Supplier.query.get(int(8))
category = Category.query.get(int(3))
p20 = Product(productname="Sir Rodney's Marmalade", supplier=supplier, category=category, unit="30 gift boxes", price=81)
db.session.add(p20)

supplier = Supplier.query.get(int(8))
category = Category.query.get(int(3))
p21 = Product(productname="Sir Rodney's Scones", supplier=supplier, category=category, unit="24 pkgs. x 4 pieces", price=10)
db.session.add(p21)

supplier = Supplier.query.get(int(9))
category = Category.query.get(int(5))
p22 = Product(productname="Gustaf's Knäckebröd", supplier=supplier, category=category, unit="24 - 500 g pkgs.", price=21)
db.session.add(p22)

supplier = Supplier.query.get(int(9))
category = Category.query.get(int(5))
p23 = Product(productname="Tunnbröd", supplier=supplier, category=category, unit="12 - 250 g pkgs.", price=9)
db.session.add(p23)

supplier = Supplier.query.get(int(10))
category = Category.query.get(int(1))
p24 = Product(productname="Guaraná Fantástica", supplier=supplier, category=category, unit="12 - 355 ml cans", price=4.5)
db.session.add(p24)

supplier = Supplier.query.get(int(11))
category = Category.query.get(int(3))
p25 = Product(productname="NuNuCa Nuß-Nougat-Creme", supplier=supplier, category=category, unit="20 - 450 g glasses", price=14)
db.session.add(p25)

supplier = Supplier.query.get(int(11))
category = Category.query.get(int(3))
p26 = Product(productname="Gumbär Gummibärchen", supplier=supplier, category=category, unit="100 - 250 g bags", price=31.23)
db.session.add(p26)

supplier = Supplier.query.get(int(11))
category = Category.query.get(int(3))
p27 = Product(productname="Schoggi Schokolade", supplier=supplier, category=category, unit="100 - 100 g pieces", price=43.9)
db.session.add(p27)

supplier = Supplier.query.get(int(12))
category = Category.query.get(int(7))
p28 = Product(productname="Rössle Sauerkraut", supplier=supplier, category=category, unit="25 - 825 g cans", price=45.6)
db.session.add(p28)

supplier = Supplier.query.get(int(12))
category = Category.query.get(int(6))
p29 = Product(productname="Thüringer Rostbratwurst", supplier=supplier, category=category, unit="50 bags x 30 sausgs.", price=123.79)
db.session.add(p29)

supplier = Supplier.query.get(int(13))
category = Category.query.get(int(8))
p30 = Product(productname="Nord-Ost Matjeshering", supplier=supplier, category=category, unit="10 - 200 g glasses", price=25.89)
db.session.add(p30)

supplier = Supplier.query.get(int(14))
category = Category.query.get(int(4))
p31 = Product(productname="Gorgonzola Telino", supplier=supplier, category=category, unit="12 - 100 g pkgs", price=12.5)
db.session.add(p31)

supplier = Supplier.query.get(int(14))
category = Category.query.get(int(4))
p32 = Product(productname="Mascarpone Fabioli", supplier=supplier, category=category, unit="24 - 200 g pkgs.", price=32)
db.session.add(p32)

supplier = Supplier.query.get(int(15))
category = Category.query.get(int(4))
p33 = Product(productname="Geitost", supplier=supplier, category=category, unit="500 g", price=2.5)
db.session.add(p33)

supplier = Supplier.query.get(int(16))
category = Category.query.get(int(1))
p34 = Product(productname="Sasquatch Ale", supplier=supplier, category=category, unit="24 - 12 oz bottles", price=14)
db.session.add(p34)

supplier = Supplier.query.get(int(16))
category = Category.query.get(int(1))
p35 = Product(productname="Steeleye Stout", supplier=supplier, category=category, unit="24 - 12 oz bottles", price=18)
db.session.add(p35)

supplier = Supplier.query.get(int(17))
category = Category.query.get(int(8))
p36 = Product(productname="Inlagd Sill", supplier=supplier, category=category, unit="24 - 250 g jars", price=19)
db.session.add(p36)

supplier = Supplier.query.get(int(17))
category = Category.query.get(int(8))
p37 = Product(productname="Gravad lax", supplier=supplier, category=category, unit="12 - 500 g pkgs.", price=26)
db.session.add(p37)

supplier = Supplier.query.get(int(18))
category = Category.query.get(int(1))
p38 = Product(productname="Côte de Blaye", supplier=supplier, category=category, unit="12 - 75 cl bottles", price=263.5)
db.session.add(p38)

supplier = Supplier.query.get(int(18))
category = Category.query.get(int(1))
p39 = Product(productname="Chartreuse verte", supplier=supplier, category=category, unit="750 cc per bottle", price=18)
db.session.add(p39)

supplier = Supplier.query.get(int(19))
category = Category.query.get(int(8))
p40 = Product(productname="Boston Crab Meat", supplier=supplier, category=category, unit="24 - 4 oz tins", price=18.4)
db.session.add(p40)

supplier = Supplier.query.get(int(19))
category = Category.query.get(int(8))
p41 = Product(productname="Jack's New England Clam Chowder", supplier=supplier, category=category, unit="12 - 12 oz cans", price=9.65)
db.session.add(p41)

supplier = Supplier.query.get(int(20))
category = Category.query.get(int(5))
p42 = Product(productname="Singaporean Hokkien Fried Mee", supplier=supplier, category=category, unit="32 - 1 kg pkgs.", price=14)
db.session.add(p42)

supplier = Supplier.query.get(int(20))
category = Category.query.get(int(1))
p43 = Product(productname="Ipoh Coffee", supplier=supplier, category=category, unit="16 - 500 g tins", price=46)
db.session.add(p43)

supplier = Supplier.query.get(int(20))
category = Category.query.get(int(2))
p44 = Product(productname="Gula Malacca", supplier=supplier, category=category, unit="20 - 2 kg bags", price=19.45)
db.session.add(p44)

supplier = Supplier.query.get(int(21))
category = Category.query.get(int(8))
p45 = Product(productname="Røgede sild", supplier=supplier, category=category, unit="1k pkg.", price=9.5)
db.session.add(p45)

supplier = Supplier.query.get(int(21))
category = Category.query.get(int(8))
p46 = Product(productname="Spegesild", supplier=supplier, category=category, unit="4 - 450 g glasses", price=12)
db.session.add(p46)

supplier = Supplier.query.get(int(22))
category = Category.query.get(int(3))
p47 = Product(productname="Zaanse koeken", supplier=supplier, category=category, unit="10 - 4 oz boxes", price=9.5)
db.session.add(p47)

supplier = Supplier.query.get(int(22))
category = Category.query.get(int(3))
p48 = Product(productname="Chocolade", supplier=supplier, category=category, unit="10 pkgs.", price=12.75)
db.session.add(p48)

supplier = Supplier.query.get(int(23))
category = Category.query.get(int(3))
p49 = Product(productname="Maxilaku", supplier=supplier, category=category, unit="24 - 50 g pkgs.", price=20)
db.session.add(p49)

supplier = Supplier.query.get(int(23))
category = Category.query.get(int(3))
p50 = Product(productname="Valkoinen suklaa", supplier=supplier, category=category, unit="12 - 100 g bars", price=16.25)
db.session.add(p50)

supplier = Supplier.query.get(int(24))
category = Category.query.get(int(7))
p51 = Product(productname="Manjimup Dried Apples", supplier=supplier, category=category, unit="50 - 300 g pkgs.", price=53)
db.session.add(p51)

supplier = Supplier.query.get(int(24))
category = Category.query.get(int(5))
p52 = Product(productname="Filo Mix", supplier=supplier, category=category, unit="16 - 2 kg boxes", price=7)
db.session.add(p52)

supplier = Supplier.query.get(int(24))
category = Category.query.get(int(6))
p53 = Product(productname="Perth Pasties", supplier=supplier, category=category, unit="48 pieces", price=32.8)
db.session.add(p53)

supplier = Supplier.query.get(int(25))
category = Category.query.get(int(6))
p54 = Product(productname="Tourtière", supplier=supplier, category=category, unit="16 pies", price=7.45)
db.session.add(p54)

supplier = Supplier.query.get(int(25))
category = Category.query.get(int(6))
p55 = Product(productname="Pâté chinois", supplier=supplier, category=category, unit="24 boxes x 2 pies", price=24)
db.session.add(p55)

supplier = Supplier.query.get(int(26))
category = Category.query.get(int(5))
p56 = Product(productname="Gnocchi di nonna Alice", supplier=supplier, category=category, unit="24 - 250 g pkgs.", price=38)
db.session.add(p56)

supplier = Supplier.query.get(int(26))
category = Category.query.get(int(5))
p57 = Product(productname="Ravioli Angelo", supplier=supplier, category=category, unit="24 - 250 g pkgs.", price=19.5)
db.session.add(p57)

supplier = Supplier.query.get(int(27))
category = Category.query.get(int(8))
p58 = Product(productname="Escargots de Bourgogne", supplier=supplier, category=category, unit="24 pieces", price=13.25)
db.session.add(p58)

supplier = Supplier.query.get(int(28))
category = Category.query.get(int(4))
p59 = Product(productname="Raclette Courdavault", supplier=supplier, category=category, unit="5 kg pkg.", price=55)
db.session.add(p59)

supplier = Supplier.query.get(int(28))
category = Category.query.get(int(4))
p60 = Product(productname="Camembert Pierrot", supplier=supplier, category=category, unit="15 - 300 g rounds", price=34)
db.session.add(p60)

supplier = Supplier.query.get(int(29))
category = Category.query.get(int(2))
p61 = Product(productname="Sirop d'érable", supplier=supplier, category=category, unit="24 - 500 ml bottles", price=28.5)
db.session.add(p61)

supplier = Supplier.query.get(int(29))
category = Category.query.get(int(3))
p62 = Product(productname="Tarte au sucre", supplier=supplier, category=category, unit="48 pies", price=49.3)
db.session.add(p62)

supplier = Supplier.query.get(int(7))
category = Category.query.get(int(2))
p63 = Product(productname="Vegie-spread", supplier=supplier, category=category, unit="15 - 625 g jars", price=43.9)
db.session.add(p63)

supplier = Supplier.query.get(int(12))
category = Category.query.get(int(5))
p64 = Product(productname="Wimmers gute Semmelknödel", supplier=supplier, category=category, unit="20 bags x 4 pieces", price=33.25)
db.session.add(p64)

supplier = Supplier.query.get(int(2))
category = Category.query.get(int(2))
p65 = Product(productname="Louisiana Fiery Hot Pepper Sauce", supplier=supplier, category=category, unit="32 - 8 oz bottles", price=21.05)
db.session.add(p65)

supplier = Supplier.query.get(int(2))
category = Category.query.get(int(2))
p66 = Product(productname="Louisiana Hot Spiced Okra", supplier=supplier, category=category, unit="24 - 8 oz jars", price=17)
db.session.add(p66)

supplier = Supplier.query.get(int(16))
category = Category.query.get(int(1))
p67 = Product(productname="Laughing Lumberjack Lager", supplier=supplier, category=category, unit="24 - 12 oz bottles", price=14)
db.session.add(p67)

supplier = Supplier.query.get(int(8))
category = Category.query.get(int(3))
p68 = Product(productname="Scottish Longbreads", supplier=supplier, category=category, unit="10 boxes x 8 pieces", price=12.5)
db.session.add(p68)

supplier = Supplier.query.get(int(15))
category = Category.query.get(int(4))
p69 = Product(productname="Gudbrandsdalsost", supplier=supplier, category=category, unit="10 kg pkg.", price=36)
db.session.add(p69)

supplier = Supplier.query.get(int(7))
category = Category.query.get(int(1))
p70 = Product(productname="Outback Lager", supplier=supplier, category=category, unit="24 - 355 ml bottles", price=15)
db.session.add(p70)

supplier = Supplier.query.get(int(15))
category = Category.query.get(int(4))
p71 = Product(productname="Fløtemysost", supplier=supplier, category=category, unit="10 - 500 g pkgs.", price=21.5)
db.session.add(p71)

supplier = Supplier.query.get(int(14))
category = Category.query.get(int(4))
p72 = Product(productname="Mozzarella di Giovanni", supplier=supplier, category=category, unit="24 - 200 g pkgs.", price=34.8)
db.session.add(p72)

supplier = Supplier.query.get(int(17))
category = Category.query.get(int(8))
p73 = Product(productname="Röd Kaviar", supplier=supplier, category=category, unit="24 - 150 g jars", price=15)
db.session.add(p73)

supplier = Supplier.query.get(int(4))
category = Category.query.get(int(7))
p74 = Product(productname="Longlife Tofu", supplier=supplier, category=category, unit="5 kg pkg.", price=10)
db.session.add(p74)

supplier = Supplier.query.get(int(12))
category = Category.query.get(int(1))
p75 = Product(productname="Rhönbräu Klosterbier", supplier=supplier, category=category, unit="24 - 0.5 l bottles", price=7.75)
db.session.add(p75)

supplier = Supplier.query.get(int(23))
category = Category.query.get(int(1))
p76 = Product(productname="Lakkalikööri", supplier=supplier, category=category, unit="500 ml ", price=18)
db.session.add(p76)

supplier = Supplier.query.get(int(12))
category = Category.query.get(int(2))
p77 = Product(productname="Original Frankfurter grüne Soße", supplier=supplier, category=category, unit="12 boxes", price=13)
db.session.add(p77)

db.session.commit()

print('Dummy products successfully added to the database!')