from datetime import datetime



print('''from datetime import datetime
from app import db
from app.models import User, Category, Supplier, Shipper, Employee\n\n\n''')


customers_array = [
    ("Alfreds Futterkiste","Maria Anders","Obere Str. 57","Berlin","12209","Germany"),
    ("Ana Trujillo Emparedados y helados","Ana Trujillo","Avda. de la Constitución 2222","México D.F.","05021","Mexico"),
    ("Antonio Moreno Taquería","Antonio Moreno","Mataderos 2312","México D.F.","05023","Mexico"),
    ("Around the Horn","Thomas Hardy","120 Hanover Sq.","London","WA1 1DP","UK"),
    ("Berglunds snabbköp","Christina Berglund","Berguvsvägen 8","Luleå","S-958 22","Sweden"),
    ("Blauer See Delikatessen","Hanna Moos","Forsterstr. 57","Mannheim","68306","Germany"),
    ("Blondel père et fils","Frédérique Citeaux","24, place Kléber","Strasbourg","67000","France"),
    ("Bólido Comidas preparadas","Martín Sommer","C/ Araquil, 67","Madrid","28023","Spain"),
    ("Bon app'","Laurence Lebihans","12, rue des Bouchers","Marseille","13008","France"),
    ("Bottom-Dollar Marketse","Elizabeth Lincoln","23 Tsawassen Blvd.","Tsawassen","T2F 8M4","Canada"),
    ("B's Beverages","Victoria Ashworth","Fauntleroy Circus","London","EC2 5NT","UK"),
    ("Cactus Comidas para llevar","Patricio Simpson","Cerrito 333","Buenos Aires","1010","Argentina"),
    ("Centro comercial Moctezuma","Francisco Chang","Sierras de Granada 9993","México D.F.","05022","Mexico"),
    ("Chop-suey Chinese","Yang Wang","Hauptstr. 29","Bern","3012","Switzerland"),
    ("Comércio Mineiro","Pedro Afonso","Av. dos Lusíadas, 23","São Paulo","05432-043","Brazil"),
    ("Consolidated Holdings","Elizabeth Brown","Berkeley Gardens 12 Brewery ","London","WX1 6LT","UK"),
    ("Drachenblut Delikatessend","Sven Ottlieb","Walserweg 21","Aachen","52066","Germany"),
    ("Du monde entier","Janine Labrune","67, rue des Cinquante Otages","Nantes","44000","France"),
    ("Eastern Connection","Ann Devon","35 King George","London","WX3 6FW","UK"),
    ("Ernst Handel","Roland Mendel","Kirchgasse 6","Graz","8010","Austria"),
    ("Familia Arquibaldo","Aria Cruz","Rua Orós, 92","São Paulo","05442-030","Brazil"),
    ("FISSA Fabrica Inter. Salchichas S.A.","Diego Roel","C/ Moralzarzal, 86","Madrid","28034","Spain"),
    ("Folies gourmandes","Martine Rancé","184, chaussée de Tournai","Lille","59000","France"),
    ("Folk och fä HB","Maria Larsson","Åkergatan 24","Bräcke","S-844 67","Sweden"),
    ("Frankenversand","Peter Franken","Berliner Platz 43","München","80805","Germany"),
    ("France restauration","Carine Schmitt","54, rue Royale","Nantes","44000","France"),
    ("Franchi S.p.A.","Paolo Accorti","Via Monte Bianco 34","Torino","10100","Italy"),
    ("Furia Bacalhau e Frutos do Mar","Lino Rodriguez ","Jardim das rosas n. 32","Lisboa","1675","Portugal"),
    ("Galería del gastrónomo","Eduardo Saavedra","Rambla de Cataluña, 23","Barcelona","08022","Spain"),
    ("Godos Cocina Típica","José Pedro Freyre","C/ Romero, 33","Sevilla","41101","Spain"),
    ("Gourmet Lanchonetes","André Fonseca","Av. Brasil, 442","Campinas","04876-786","Brazil"),
    ("Great Lakes Food Market","Howard Snyder","2732 Baker Blvd.","Eugene","97403","USA"),
    ("GROSELLA-Restaurante","Manuel Pereira","5ª Ave. Los Palos Grandes","Caracas","1081","Venezuela"),
    ("Hanari Carnes","Mario Pontes","Rua do Paço, 67","Rio de Janeiro","05454-876","Brazil"),
    ("HILARIÓN-Abastos","Carlos Hernández","Carrera 22 con Ave. Carlos Soublette #8-35","San Cristóbal","5022","Venezuela"),
    ("Hungry Coyote Import Store","Yoshi Latimer","City Center Plaza 516 Main St.","Elgin","97827","USA"),
    ("Hungry Owl All-Night Grocers","Patricia McKenna","8 Johnstown Road","Cork","","Ireland"),
    ("Island Trading","Helen Bennett","Garden House Crowther Way","Cowes","PO31 7PJ","UK"),
    ("Königlich Essen","Philip Cramer","Maubelstr. 90","Brandenburg","14776","Germany"),
    ("La corne d'abondance","Daniel Tonini","67, avenue de l'Europe","Versailles","78000","France"),
    ("La maison d'Asie","Annette Roulet","1 rue Alsace-Lorraine","Toulouse","31000","France"),
    ("Laughing Bacchus Wine Cellars","Yoshi Tannamuri","1900 Oak St.","Vancouver","V3F 2K1","Canada"),
    ("Lazy K Kountry Store","John Steel","12 Orchestra Terrace","Walla Walla","99362","USA"),
    ("Lehmanns Marktstand","Renate Messner","Magazinweg 7","Frankfurt a.M. ","60528","Germany"),
    ("Let's Stop N Shop","Jaime Yorres","87 Polk St. Suite 5","San Francisco","94117","USA"),
    ("LILA-Supermercado","Carlos González","Carrera 52 con Ave. Bolívar #65-98 Llano Largo","Barquisimeto","3508","Venezuela"),
    ("LINO-Delicateses","Felipe Izquierdo","Ave. 5 de Mayo Porlamar","I. de Margarita","4980","Venezuela"),
    ("Lonesome Pine Restaurant","Fran Wilson","89 Chiaroscuro Rd.","Portland","97219","USA"),
    ("Magazzini Alimentari Riuniti","Giovanni Rovelli","Via Ludovico il Moro 22","Bergamo","24100","Italy"),
    ("Maison Dewey","Catherine Dewey","Rue Joseph-Bens 532","Bruxelles","B-1180","Belgium"),
    ("Mère Paillarde","Jean Fresnière","43 rue St. Laurent","Montréal","H1J 1C3","Canada"),
    ("Morgenstern Gesundkost","Alexander Feuer","Heerstr. 22","Leipzig","04179","Germany"),
    ("North/South","Simon Crowther","South House 300 Queensbridge","London","SW7 1RZ","UK"),
    ("Océano Atlántico Ltda.","Yvonne Moncada","Ing. Gustavo Moncada 8585 Piso 20-A","Buenos Aires","1010","Argentina"),
    ("Old World Delicatessen","Rene Phillips","2743 Bering St.","Anchorage","99508","USA"),
    ("Ottilies Käseladen","Henriette Pfalzheim","Mehrheimerstr. 369","Köln","50739","Germany"),
    ("Paris spécialités","Marie Bertrand","265, boulevard Charonne","Paris","75012","France"),
    ("Pericles Comidas clásicas","Guillermo Fernández","Calle Dr. Jorge Cash 321","México D.F.","05033","Mexico"),
    ("Piccolo und mehr","Georg Pipps","Geislweg 14","Salzburg","5020","Austria"),
    ("Princesa Isabel Vinhoss","Isabel de Castro","Estrada da saúde n. 58","Lisboa","1756","Portugal"),
    ("Que Delícia","Bernardo Batista","Rua da Panificadora, 12","Rio de Janeiro","02389-673","Brazil"),
    ("Queen Cozinha","Lúcia Carvalho","Alameda dos Canàrios, 891","São Paulo","05487-020","Brazil"),
    ("QUICK-Stop","Horst Kloss","Taucherstraße 10","Cunewalde","01307","Germany"),
    ("Rancho grande","Sergio Gutiérrez","Av. del Libertador 900","Buenos Aires","1010","Argentina"),
    ("Rattlesnake Canyon Grocery","Paula Wilson","2817 Milton Dr.","Albuquerque","87110","USA"),
    ("Reggiani Caseifici","Maurizio Moroni","Strada Provinciale 124","Reggio Emilia","42100","Italy"),
    ("Ricardo Adocicados","Janete Limeira","Av. Copacabana, 267","Rio de Janeiro","02389-890","Brazil"),
    ("Richter Supermarkt","Michael Holz","Grenzacherweg 237","Genève","1203","Switzerland"),
    ("Romero y tomillo","Alejandra Camino","Gran Vía, 1","Madrid","28001","Spain"),
    ("Santé Gourmet","Jonas Bergulfsen","Erling Skakkes gate 78","Stavern","4110","Norway"),
    ("Save-a-lot Markets","Jose Pavarotti","187 Suffolk Ln.","Boise","83720","USA"),
    ("Seven Seas Imports","Hari Kumar","90 Wadhurst Rd.","London","OX15 4NB","UK"),
    ("Simons bistro","Jytte Petersen","Vinbæltet 34","København","1734","Denmark"),
    ("Spécialités du monde","Dominique Perrier","25, rue Lauriston","Paris","75016","France"),
    ("Split Rail Beer & Ale","Art Braunschweiger","P.O. Box 555","Lander","82520","USA"),
    ("Suprêmes délices","Pascale Cartrain","Boulevard Tirou, 255","Charleroi","B-6000","Belgium"),
    ("The Big Cheese","Liz Nixon","89 Jefferson Way Suite 2","Portland","97201","USA"),
    ("The Cracker Box","Liu Wong","55 Grizzly Peak Rd.","Butte","59801","USA"),
    ("Toms Spezialitäten","Karin Josephs","Luisenstr. 48","Münster","44087","Germany"),
    ("Tortuga Restaurante","Miguel Angel Paolino","Avda. Azteca 123","México D.F.","05033","Mexico"),
    ("Tradição Hipermercados","Anabela Domingues","Av. Inês de Castro, 414","São Paulo","05634-030","Brazil"),
    ("Trail's Head Gourmet Provisioners","Helvetius Nagy","722 DaVinci Blvd.","Kirkland","98034","USA"),
    ("Vaffeljernet","Palle Ibsen","Smagsløget 45","Århus","8200","Denmark"),
    ("Victuailles en stock","Mary Saveley","2, rue du Commerce","Lyon","69004","France"),
    ("Vins et alcools Chevalier","Paul Henriot","59 rue de l'Abbaye","Reims","51100","France"),
    ("Die Wandernde Kuh","Rita Müller","Adenauerallee 900","Stuttgart","70563","Germany"),
    ("Wartian Herkku","Pirkko Koskitalo","Torikatu 38","Oulu","90110","Finland"),
    ("Wellington Importadora","Paula Parente","Rua do Mercado, 12","Resende","08737-363","Brazil"),
    ("White Clover Markets","Karl Jablonski","305 - 14th Ave. S. Suite 3B","Seattle","98128","USA"),
    ("Wilman Kala","Matti Karttunen","Keskuskatu 45","Helsinki","21240","Finland"),
    ("Wolski","Zbyszek","ul. Filtrowa 68","Walla","01-012","Poland")
]


for u in customers_array:
    #Separate the names data into lastname, middlename, firstname
    name_list = u[1].split()
    firstname = name_list[0]
    #Make up usernames from the given contact names
    username = u[1].replace(" ", "")
    #Make up dummy emails from the given customer names
    email = u[0].replace(" ", "") + "@example.com"
    if len(name_list) > 2:
        middlename = name_list[1]
        lastname = name_list[2]
        middlenameinsert = 'middlename="' + middlename +  '"'
        lastnameinsert = 'lastname="' + lastname +  '"'
    else:
        middlename = None
        lastname = None
        middlenameinsert = 'middlename=None'
        lastnameinsert = 'lastname=None'
    print('''u{} = User(username="{}",customername="{}",{},{},firstname="{}",email="{}",address="{}",city="{}",postalcode="{}",country="{}")\nu{}.set_password("{}")\ndb.session.add(u{})'''
        .format(
            customers_array.index(u),
            username, u[0], lastnameinsert, middlenameinsert,
            firstname, email, u[2], u[3], u[4],
            u[5], customers_array.index(u), firstname, customers_array.index(u)
        )
    )
print('db.session.commit()\n\n\n')



suppliers_array = [
    (1,"Exotic Liquid","Charlotte Cooper","49 Gilbert St.","Londona","EC1 4SD","UK","(171) 555-2222"),
    (2,"New Orleans Cajun Delights","Shelley Burke","P.O. Box 78934","New Orleans","70117","USA","(100) 555-4822"),
    (3,"Grandma Kelly's Homestead","Regina Murphy","707 Oxford Rd.","Ann Arbor","48104","USA","(313) 555-5735"),
    (4,"Tokyo Traders","Yoshi Nagase","9-8 Sekimai Musashino-shi","Tokyo","100","Japan","(03) 3555-5011"),
    (5,"Cooperativa de Quesos 'Las Cabras'","Antonio del Valle Saavedra ","Calle del Rosal 4","Oviedo","33007","Spain","(98) 598 76 54"),
    (6,"Mayumi's","Mayumi Ohno","92 Setsuko Chuo-ku","Osaka","545","Japan","(06) 431-7877"),
    (7,"Pavlova, Ltd.","Ian Devling","74 Rose St. Moonie Ponds","Melbourne","3058","Australia","(03) 444-2343"),
    (8,"Specialty Biscuits, Ltd.","Peter Wilson","29 King's Way","Manchester","M14 GSD","UK","(161) 555-4448"),
    (9,"PB Knäckebröd AB","Lars Peterson","Kaloadagatan 13","Göteborg","S-345 67","Sweden ","031-987 65 43"),
    (10,"Refrescos Americanas LTDA","Carlos Diaz","Av. das Americanas 12.890","São Paulo","5442","Brazil","(11) 555 4640"),
    (11,"Heli Süßwaren GmbH &amp; Co. KG","Petra Winkler","Tiergartenstraße 5","Berlin","10785","Germany","(010) 9984510"),
    (12,"Plutzer Lebensmittelgroßmärkte AG","Martin Bein","Bogenallee 51","Frankfurt","60439","Germany","(069) 992755"),
    (13,"Nord-Ost-Fisch Handelsgesellschaft mbH","Sven Petersen","Frahmredder 112a","Cuxhaven","27478","Germany","(04721) 8713"),
    (14,"Formaggi Fortini s.r.l.","Elio Rossi","Viale Dante, 75","Ravenna","48100","Italy","(0544) 60323"),
    (15,"Norske Meierier","Beate Vileid","Hatlevegen 5","Sandvika","1320","Norway","(0)2-953010"),
    (16,"Bigfoot Breweries","Cheryl Saylor","3400 - 8th Avenue Suite 210","Bend","97101","USA","(503) 555-9931"),
    (17,"Svensk Sjöföda AB","Michael Björn","Brovallavägen 231","Stockholm","S-123 45","Sweden","08-123 45 67"),
    (18,"Aux joyeux ecclésiastiques","Guylène Nodier","203, Rue des Francs-Bourgeois","Paris","75004","France","(1) 03.83.00.68"),
    (19,"New England Seafood Cannery","Robb Merchant","Order Processing Dept. 2100 Paul Revere Blvd.","Boston","02134","USA","(617) 555-3267"),
    (20,"Leka Trading","Chandra Leka","471 Serangoon Loop, Suite #402","Singapore","0512","Singapore","555-8787"),
    (21,"Lyngbysild","Niels Petersen","Lyngbysild Fiskebakken 10","Lyngby","2800","Denmark","43844108"),
    (22,"Zaanse Snoepfabriek","Dirk Luchte","Verkoop Rijnweg 22","Zaandam","9999 ZZ","Netherlands","(12345) 1212"),
    (23,"Karkki Oy","Anne Heikkonen","Valtakatu 12","Lappeenranta","53120","Finland","(953) 10956"),
    (24,"G'day, Mate","Wendy Mackenzie","170 Prince Edward Parade Hunter's Hill","Sydney","2042","Australia","(02) 555-5914"),
    (25,"Ma Maison","Jean-Guy Lauzon","2960 Rue St. Laurent","Montréal","H1J 1C3","Canada","(514) 555-9022"),
    (26,"Pasta Buttini s.r.l.","Giovanni Giudici","Via dei Gelsomini, 153","Salerno","84100","Italy","(089) 6547665"),
    (27,"Escargots Nouveaux","Marie Delamare","22, rue H. Voiron","Montceau","71300","France","85.57.00.07"),
    (28,"Gai pâturage","Eliane Noz","Bat. B 3, rue des Alpes","Annecy","74000","France","38.76.98.06"),
    (29,"Forêts d'érables","Chantal Goulet","148 rue Chasseur","Ste-Hyacinthe","J2S 7S8","Canada","(514) 555-2955")
]

for su in suppliers_array:
    print('su{} = Supplier(suppliername="{}",contactname="{}",address="{}",city="{}",postalcode="{}",country="{}",phone="{}")\ndb.session.add(su{})'
        .format(su[0], su[1], su[2], su[3], su[4], su[5], su[6], su[7], su[0]))
print('db.session.commit()\n\n\n')




employees_array = [
    ("Davolio","Nancy","1968-12-08","EmpID1.pic","""Education includes a BA in psychology from Colorado State University. She also completed (The Art of the Cold Call). Nancy is a member of 'Toastmasters International'."""),
    ("Fuller","Andrew","1952-02-19","EmpID2.pic","""Andrew received his BTS commercial and a Ph.D. in international marketing from the University of Dallas. He is fluent in French and Italian and reads German. He joined the company as a sales representative, was promoted to sales manager and was then named vice president of sales. Andrew is a member of the Sales Management Roundtable, the Seattle Chamber of Commerce, and the Pacific Rim Importers Association."""),
    ("Leverling","Janet","1963-08-30","EmpID3.pic","""Janet has a BS degree in chemistry from Boston College). She has also completed a certificate program in food retailing management. Janet was hired as a sales associate and was promoted to sales representative."""),
    ("Peacock","Margaret","1958-09-19","EmpID4.pic","""Margaret holds a BA in English literature from Concordia College and an MA from the American Institute of Culinary Arts. She was temporarily assigned to the London office before returning to her permanent post in Seattle."""),
    ("Buchanan","Steven","1955-03-04","EmpID5.pic","""Steven Buchanan graduated from St. Andrews University, Scotland, with a BSC degree. Upon joining the company as a sales representative, he spent 6 months in an orientation program at the Seattle office and then returned to his permanent post in London, where he was promoted to sales manager. Mr. Buchanan has completed the courses 'Successful Telemarketing' and 'International Sales Management'. He is fluent in French."""),
    ("Suyama","Michael","1963-07-02","EmpID6.pic","""Michael is a graduate of Sussex University (MA, economics) and the University of California at Los Angeles (MBA, marketing). He has also taken the courses 'Multi-Cultural Selling' and 'Time Management for the Sales Professional'. He is fluent in Japanese and can read and write French, Portuguese, and Spanish."""),
    ("King","Robert","1960-05-29","EmpID7.pic","""Robert King served in the Peace Corps and traveled extensively before completing his degree in English at the University of Michigan and then joining the company. After completing a course entitled 'Selling in Europe', he was transferred to the London office."""),
    ("Callahan","Laura","1958-01-09","EmpID8.pic","""Laura received a BA in psychology from the University of Washington. She has also completed a course in business French. She reads and writes French."""),
    ("Dodsworth","Anne","1969-07-02","EmpID9.pic","""Anne has a BA degree in English from St. Lawrence College. She is fluent in French and German."""),
    ("West","Adam","1928-09-19","EmpID10.pic","""An old chum.""")
]

formatted_date_employees_array = [

]


for e in employees_array:
    date = e[2].split("-")
    formatted_date = datetime(int(date[0]), int(date[1]), int(date[2]))
    formatted_date_employee = (e[0], e[1], formatted_date, e[3], e[4])
    formatted_date_employees_array.append(formatted_date_employee)


for e in formatted_date_employees_array:
    print('e{} = Employee(lastname="{}",firstname="{}",notes="{}")\ndb.session.add(e{})'
          .format(formatted_date_employees_array.index(e), e[0], e[1], e[4], formatted_date_employees_array.index(e)))
print('db.session.commit()\n\n\n')



categories_array = [
    ("Beverages","Soft drinks, coffees, teas, beers, and ales"),
    ("Condiments","Sweet and savory sauces, relishes, spreads, and seasonings"),
    ("Confections","Desserts, candies, and sweet breads"),
    ("Dairy Products","Cheeses"),
    ("Grains/Cereals","Breads, crackers, pasta, and cereal"),
    ("Meat/Poultry","Prepared meats"),
    ("Produce","Dried fruit and bean curd"),
    ("Seafood","Seaweed and fish")
]


for c in categories_array:
    print('c{} = Category(categoryname="{}",description="{}")\ndb.session.add(c{})'
        .format(categories_array.index(c), c[0], c[1], categories_array.index(c)))
print('db.session.commit()\n\n\n')



shippers_array = [
    (1,"Speedy Express","(503) 555-9831"),
    (2,"United Package","(503) 555-3199"),
    (3,"Federal Shipping","(503) 555-9931")
]


for s in shippers_array:
    print('s{} = Shipper(shippername="{}",phone="{}")\ndb.session.add(s{})'.format(s[0], s[1], s[2], s[0]))
print('db.session.commit()\n\n')

