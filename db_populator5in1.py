from datetime import datetime
from app import db
from app.models import User, Category, Supplier, Shipper, Employee



u0 = User(
         username="MariaAnders", customername="Alfreds Futterkiste", lastname=None, middlename=None,
        firstname="Maria", email="AlfredsFutterkiste@example.com", address="Obere Str. 57", city="Berlin", postalcode="12209",
        country="Germany")
db.session.add(u0)
u1 = User(
        username="AnaTrujillo", customername="Ana Trujillo Emparedados y helados", lastname=None, middlename=None,
        firstname="Ana", email="AnaTrujilloEmparedadosyhelados@example.com", address="Avda. de la Constitución 2222", city="México D.F.", postalcode="05021",
        country="Mexico")
db.session.add(u1)
u2 = User(
        username="AntonioMoreno", customername="Antonio Moreno Taquería", lastname=None, middlename=None,
        firstname="Antonio", email="AntonioMorenoTaquería@example.com", address="Mataderos 2312", city="México D.F.", postalcode="05023",
        country="Mexico")
db.session.add(u2)
u3 = User(
        username="ThomasHardy", customername="Around the Horn", lastname=None, middlename=None,
        firstname="Thomas", email="AroundtheHorn@example.com", address="120 Hanover Sq.", city="London", postalcode="WA1 1DP",
        country="UK")
db.session.add(u3)
u4 = User(
        username="ChristinaBerglund", customername="Berglunds snabbköp", lastname=None, middlename=None,
        firstname="Christina", email="Berglundssnabbköp@example.com", address="Berguvsvägen 8", city="Luleå", postalcode="S-958 22",
        country="Sweden")
db.session.add(u4)
u5 = User(
        username="HannaMoos", customername="Blauer See Delikatessen", lastname=None, middlename=None,
        firstname="Hanna", email="BlauerSeeDelikatessen@example.com", address="Forsterstr. 57", city="Mannheim", postalcode="68306",
        country="Germany")
db.session.add(u5)
u6 = User(
        username="FrédériqueCiteaux", customername="Blondel père et fils", lastname=None, middlename=None,
        firstname="Frédérique", email="Blondelpèreetfils@example.com", address="24, place Kléber", city="Strasbourg", postalcode="67000",
        country="France")
db.session.add(u6)
u7 = User(
        username="MartínSommer", customername="Bólido Comidas preparadas", lastname=None, middlename=None,
        firstname="Martín", email="BólidoComidaspreparadas@example.com", address="C/ Araquil, 67", city="Madrid", postalcode="28023",
        country="Spain")
db.session.add(u7)
u8 = User(
        username="LaurenceLebihans", customername="Bon app'", lastname=None, middlename=None,
        firstname="Laurence", email="Bonapp'@example.com", address="12, rue des Bouchers", city="Marseille", postalcode="13008",
        country="France")
db.session.add(u8)
u9 = User(
        username="ElizabethLincoln", customername="Bottom-Dollar Marketse", lastname=None, middlename=None,
        firstname="Elizabeth", email="Bottom-DollarMarketse@example.com", address="23 Tsawassen Blvd.", city="Tsawassen", postalcode="T2F 8M4",
        country="Canada")
db.session.add(u9)
u10 = User(
        username="VictoriaAshworth", customername="B's Beverages", lastname=None, middlename=None,
        firstname="Victoria", email="B'sBeverages@example.com", address="Fauntleroy Circus", city="London", postalcode="EC2 5NT",
        country="UK")
db.session.add(u10)
u11 = User(
        username="PatricioSimpson", customername="Cactus Comidas para llevar", lastname=None, middlename=None,
        firstname="Patricio", email="CactusComidasparallevar@example.com", address="Cerrito 333", city="Buenos Aires", postalcode="1010",
        country="Argentina")
db.session.add(u11)
u12 = User(
        username="FranciscoChang", customername="Centro comercial Moctezuma", lastname=None, middlename=None,
        firstname="Francisco", email="CentrocomercialMoctezuma@example.com", address="Sierras de Granada 9993", city="México D.F.", postalcode="05022",
        country="Mexico")
db.session.add(u12)
u13 = User(
        username="YangWang", customername="Chop-suey Chinese", lastname=None, middlename=None,
        firstname="Yang", email="Chop-sueyChinese@example.com", address="Hauptstr. 29", city="Bern", postalcode="3012",
        country="Switzerland")
db.session.add(u13)
u14 = User(
        username="PedroAfonso", customername="Comércio Mineiro", lastname=None, middlename=None,
        firstname="Pedro", email="ComércioMineiro@example.com", address="Av. dos Lusíadas, 23", city="São Paulo", postalcode="05432-043",
        country="Brazil")
db.session.add(u14)
u15 = User(
        username="ElizabethBrown", customername="Consolidated Holdings", lastname=None, middlename=None,
        firstname="Elizabeth", email="ConsolidatedHoldings@example.com", address="Berkeley Gardens 12 Brewery ", city="London", postalcode="WX1 6LT",
        country="UK")
db.session.add(u15)
u16 = User(
        username="SvenOttlieb", customername="Drachenblut Delikatessend", lastname=None, middlename=None,
        firstname="Sven", email="DrachenblutDelikatessend@example.com", address="Walserweg 21", city="Aachen", postalcode="52066",
        country="Germany")
db.session.add(u16)
u17 = User(
        username="JanineLabrune", customername="Du monde entier", lastname=None, middlename=None,
        firstname="Janine", email="Dumondeentier@example.com", address="67, rue des Cinquante Otages", city="Nantes", postalcode="44000",
        country="France")
db.session.add(u17)
u18 = User(
        username="AnnDevon", customername="Eastern Connection", lastname=None, middlename=None,
        firstname="Ann", email="EasternConnection@example.com", address="35 King George", city="London", postalcode="WX3 6FW",
        country="UK")
db.session.add(u18)
u19 = User(
        username="RolandMendel", customername="Ernst Handel", lastname=None, middlename=None,
        firstname="Roland", email="ErnstHandel@example.com", address="Kirchgasse 6", city="Graz", postalcode="8010",
        country="Austria")
db.session.add(u19)
u20 = User(
        username="AriaCruz", customername="Familia Arquibaldo", lastname=None, middlename=None,
        firstname="Aria", email="FamiliaArquibaldo@example.com", address="Rua Orós, 92", city="São Paulo", postalcode="05442-030",
        country="Brazil")
db.session.add(u20)
u21 = User(
        username="DiegoRoel", customername="FISSA Fabrica Inter. Salchichas S.A.", lastname=None, middlename=None,
        firstname="Diego", email="FISSAFabricaInter.SalchichasS.A.@example.com", address="C/ Moralzarzal, 86", city="Madrid", postalcode="28034",
        country="Spain")
db.session.add(u21)
u22 = User(
        username="MartineRancé", customername="Folies gourmandes", lastname=None, middlename=None,
        firstname="Martine", email="Foliesgourmandes@example.com", address="184, chaussée de Tournai", city="Lille", postalcode="59000",
        country="France")
db.session.add(u22)
u23 = User(
        username="MariaLarsson", customername="Folk och fä HB", lastname=None, middlename=None,
        firstname="Maria", email="FolkochfäHB@example.com", address="Åkergatan 24", city="Bräcke", postalcode="S-844 67",
        country="Sweden")
db.session.add(u23)
u24 = User(
        username="PeterFranken", customername="Frankenversand", lastname=None, middlename=None,
        firstname="Peter", email="Frankenversand@example.com", address="Berliner Platz 43", city="München", postalcode="80805",
        country="Germany")
db.session.add(u24)
u25 = User(
        username="CarineSchmitt", customername="France restauration", lastname=None, middlename=None,
        firstname="Carine", email="Francerestauration@example.com", address="54, rue Royale", city="Nantes", postalcode="44000",
        country="France")
db.session.add(u25)
u26 = User(
        username="PaoloAccorti", customername="Franchi S.p.A.", lastname=None, middlename=None,
        firstname="Paolo", email="FranchiS.p.A.@example.com", address="Via Monte Bianco 34", city="Torino", postalcode="10100",
        country="Italy")
db.session.add(u26)
u27 = User(
        username="LinoRodriguez", customername="Furia Bacalhau e Frutos do Mar", lastname=None, middlename=None,
        firstname="Lino", email="FuriaBacalhaueFrutosdoMar@example.com", address="Jardim das rosas n. 32", city="Lisboa", postalcode="1675",
        country="Portugal")
db.session.add(u27)
u28 = User(
        username="EduardoSaavedra", customername="Galería del gastrónomo", lastname=None, middlename=None,
        firstname="Eduardo", email="Galeríadelgastrónomo@example.com", address="Rambla de Cataluña, 23", city="Barcelona", postalcode="08022",
        country="Spain")
db.session.add(u28)
u29 = User(
        username="JoséPedroFreyre", customername="Godos Cocina Típica", lastname="Freyre", middlename="Pedro",
        firstname="José", email="GodosCocinaTípica@example.com", address="C/ Romero, 33", city="Sevilla", postalcode="41101",
        country="Spain")
db.session.add(u29)
u30 = User(
        username="AndréFonseca", customername="Gourmet Lanchonetes", lastname=None, middlename=None,
        firstname="André", email="GourmetLanchonetes@example.com", address="Av. Brasil, 442", city="Campinas", postalcode="04876-786",
        country="Brazil")
db.session.add(u30)
u31 = User(
        username="HowardSnyder", customername="Great Lakes Food Market", lastname=None, middlename=None,
        firstname="Howard", email="GreatLakesFoodMarket@example.com", address="2732 Baker Blvd.", city="Eugene", postalcode="97403",
        country="USA")
db.session.add(u31)
u32 = User(
        username="ManuelPereira", customername="GROSELLA-Restaurante", lastname=None, middlename=None,
        firstname="Manuel", email="GROSELLA-Restaurante@example.com", address="5ª Ave. Los Palos Grandes", city="Caracas", postalcode="1081",
        country="Venezuela")
db.session.add(u32)
u33 = User(
        username="MarioPontes", customername="Hanari Carnes", lastname=None, middlename=None,
        firstname="Mario", email="HanariCarnes@example.com", address="Rua do Paço, 67", city="Rio de Janeiro", postalcode="05454-876",
        country="Brazil")
db.session.add(u33)
u34 = User(
        username="CarlosHernández", customername="HILARIÓN-Abastos", lastname=None, middlename=None,
        firstname="Carlos", email="HILARIÓN-Abastos@example.com", address="Carrera 22 con Ave. Carlos Soublette #8-35", city="San Cristóbal", postalcode="5022",
        country="Venezuela")
db.session.add(u34)
u35 = User(
        username="YoshiLatimer", customername="Hungry Coyote Import Store", lastname=None, middlename=None,
        firstname="Yoshi", email="HungryCoyoteImportStore@example.com", address="City Center Plaza 516 Main St.", city="Elgin", postalcode="97827",
        country="USA")
db.session.add(u35)
u36 = User(
        username="PatriciaMcKenna", customername="Hungry Owl All-Night Grocers", lastname=None, middlename=None,
        firstname="Patricia", email="HungryOwlAll-NightGrocers@example.com", address="8 Johnstown Road", city="Cork", postalcode="",
        country="Ireland")
db.session.add(u36)
u37 = User(
        username="HelenBennett", customername="Island Trading", lastname=None, middlename=None,
        firstname="Helen", email="IslandTrading@example.com", address="Garden House Crowther Way", city="Cowes", postalcode="PO31 7PJ",
        country="UK")
db.session.add(u37)
u38 = User(
        username="PhilipCramer", customername="Königlich Essen", lastname=None, middlename=None,
        firstname="Philip", email="KöniglichEssen@example.com", address="Maubelstr. 90", city="Brandenburg", postalcode="14776",
        country="Germany")
db.session.add(u38)
u39 = User(
        username="DanielTonini", customername="La corne d'abondance", lastname=None, middlename=None,
        firstname="Daniel", email="Lacorned'abondance@example.com", address="67, avenue de l'Europe", city="Versailles", postalcode="78000",
        country="France")
db.session.add(u39)
u40 = User(
        username="AnnetteRoulet", customername="La maison d'Asie", lastname=None, middlename=None,
        firstname="Annette", email="Lamaisond'Asie@example.com", address="1 rue Alsace-Lorraine", city="Toulouse", postalcode="31000",
        country="France")
db.session.add(u40)
u41 = User(
        username="YoshiTannamuri", customername="Laughing Bacchus Wine Cellars", lastname=None, middlename=None,
        firstname="Yoshi", email="LaughingBacchusWineCellars@example.com", address="1900 Oak St.", city="Vancouver", postalcode="V3F 2K1",
        country="Canada")
db.session.add(u41)
u42 = User(
        username="JohnSteel", customername="Lazy K Kountry Store", lastname=None, middlename=None,
        firstname="John", email="LazyKKountryStore@example.com", address="12 Orchestra Terrace", city="Walla Walla", postalcode="99362",
        country="USA")
db.session.add(u42)
u43 = User(
        username="RenateMessner", customername="Lehmanns Marktstand", lastname=None, middlename=None,
        firstname="Renate", email="LehmannsMarktstand@example.com", address="Magazinweg 7", city="Frankfurt a.M. ", postalcode="60528",
        country="Germany")
db.session.add(u43)
u44 = User(
        username="JaimeYorres", customername="Let's Stop N Shop", lastname=None, middlename=None,
        firstname="Jaime", email="Let'sStopNShop@example.com", address="87 Polk St. Suite 5", city="San Francisco", postalcode="94117",
        country="USA")
db.session.add(u44)
u45 = User(
        username="CarlosGonzález", customername="LILA-Supermercado", lastname=None, middlename=None,
        firstname="Carlos", email="LILA-Supermercado@example.com", address="Carrera 52 con Ave. Bolívar #65-98 Llano Largo", city="Barquisimeto", postalcode="3508",
        country="Venezuela")
db.session.add(u45)
u46 = User(
        username="FelipeIzquierdo", customername="LINO-Delicateses", lastname=None, middlename=None,
        firstname="Felipe", email="LINO-Delicateses@example.com", address="Ave. 5 de Mayo Porlamar", city="I. de Margarita", postalcode="4980",
        country="Venezuela")
db.session.add(u46)
u47 = User(
        username="FranWilson", customername="Lonesome Pine Restaurant", lastname=None, middlename=None,
        firstname="Fran", email="LonesomePineRestaurant@example.com", address="89 Chiaroscuro Rd.", city="Portland", postalcode="97219",
        country="USA")
db.session.add(u47)
u48 = User(
        username="GiovanniRovelli", customername="Magazzini Alimentari Riuniti", lastname=None, middlename=None,
        firstname="Giovanni", email="MagazziniAlimentariRiuniti@example.com", address="Via Ludovico il Moro 22", city="Bergamo", postalcode="24100",
        country="Italy")
db.session.add(u48)
u49 = User(
        username="CatherineDewey", customername="Maison Dewey", lastname=None, middlename=None,
        firstname="Catherine", email="MaisonDewey@example.com", address="Rue Joseph-Bens 532", city="Bruxelles", postalcode="B-1180",
        country="Belgium")
db.session.add(u49)
u50 = User(
        username="JeanFresnière", customername="Mère Paillarde", lastname=None, middlename=None,
        firstname="Jean", email="MèrePaillarde@example.com", address="43 rue St. Laurent", city="Montréal", postalcode="H1J 1C3",
        country="Canada")
db.session.add(u50)
u51 = User(
        username="AlexanderFeuer", customername="Morgenstern Gesundkost", lastname=None, middlename=None,
        firstname="Alexander", email="MorgensternGesundkost@example.com", address="Heerstr. 22", city="Leipzig", postalcode="04179",
        country="Germany")
db.session.add(u51)
u52 = User(
        username="SimonCrowther", customername="North/South", lastname=None, middlename=None,
        firstname="Simon", email="North/South@example.com", address="South House 300 Queensbridge", city="London", postalcode="SW7 1RZ",
        country="UK")
db.session.add(u52)
u53 = User(
        username="YvonneMoncada", customername="Océano Atlántico Ltda.", lastname=None, middlename=None,
        firstname="Yvonne", email="OcéanoAtlánticoLtda.@example.com", address="Ing. Gustavo Moncada 8585 Piso 20-A", city="Buenos Aires", postalcode="1010",
        country="Argentina")
db.session.add(u53)
u54 = User(
        username="RenePhillips", customername="Old World Delicatessen", lastname=None, middlename=None,
        firstname="Rene", email="OldWorldDelicatessen@example.com", address="2743 Bering St.", city="Anchorage", postalcode="99508",
        country="USA")
db.session.add(u54)
u55 = User(
        username="HenriettePfalzheim", customername="Ottilies Käseladen", lastname=None, middlename=None,
        firstname="Henriette", email="OttiliesKäseladen@example.com", address="Mehrheimerstr. 369", city="Köln", postalcode="50739",
        country="Germany")
db.session.add(u55)
u56 = User(
        username="MarieBertrand", customername="Paris spécialités", lastname=None, middlename=None,
        firstname="Marie", email="Parisspécialités@example.com", address="265, boulevard Charonne", city="Paris", postalcode="75012",
        country="France")
db.session.add(u56)
u57 = User(
        username="GuillermoFernández", customername="Pericles Comidas clásicas", lastname=None, middlename=None,
        firstname="Guillermo", email="PericlesComidasclásicas@example.com", address="Calle Dr. Jorge Cash 321", city="México D.F.", postalcode="05033",
        country="Mexico")
db.session.add(u57)
u58 = User(
        username="GeorgPipps", customername="Piccolo und mehr", lastname=None, middlename=None,
        firstname="Georg", email="Piccoloundmehr@example.com", address="Geislweg 14", city="Salzburg", postalcode="5020",
        country="Austria")
db.session.add(u58)
u59 = User(
        username="IsabeldeCastro", customername="Princesa Isabel Vinhoss", lastname="Castro", middlename="de",
        firstname="Isabel", email="PrincesaIsabelVinhoss@example.com", address="Estrada da saúde n. 58", city="Lisboa", postalcode="1756",
        country="Portugal")
db.session.add(u59)
u60 = User(
        username="BernardoBatista", customername="Que Delícia", lastname=None, middlename=None,
        firstname="Bernardo", email="QueDelícia@example.com", address="Rua da Panificadora, 12", city="Rio de Janeiro", postalcode="02389-673",
        country="Brazil")
db.session.add(u60)
u61 = User(
        username="LúciaCarvalho", customername="Queen Cozinha", lastname=None, middlename=None,
        firstname="Lúcia", email="QueenCozinha@example.com", address="Alameda dos Canàrios, 891", city="São Paulo", postalcode="05487-020",
        country="Brazil")
db.session.add(u61)
u62 = User(
        username="HorstKloss", customername="QUICK-Stop", lastname=None, middlename=None,
        firstname="Horst", email="QUICK-Stop@example.com", address="Taucherstraße 10", city="Cunewalde", postalcode="01307",
        country="Germany")
db.session.add(u62)
u63 = User(
        username="SergioGutiérrez", customername="Rancho grande", lastname=None, middlename=None,
        firstname="Sergio", email="Ranchogrande@example.com", address="Av. del Libertador 900", city="Buenos Aires", postalcode="1010",
        country="Argentina")
db.session.add(u63)
u64 = User(
        username="PaulaWilson", customername="Rattlesnake Canyon Grocery", lastname=None, middlename=None,
        firstname="Paula", email="RattlesnakeCanyonGrocery@example.com", address="2817 Milton Dr.", city="Albuquerque", postalcode="87110",
        country="USA")
db.session.add(u64)
u65 = User(
        username="MaurizioMoroni", customername="Reggiani Caseifici", lastname=None, middlename=None,
        firstname="Maurizio", email="ReggianiCaseifici@example.com", address="Strada Provinciale 124", city="Reggio Emilia", postalcode="42100",
        country="Italy")
db.session.add(u65)
u66 = User(
        username="JaneteLimeira", customername="Ricardo Adocicados", lastname=None, middlename=None,
        firstname="Janete", email="RicardoAdocicados@example.com", address="Av. Copacabana, 267", city="Rio de Janeiro", postalcode="02389-890",
        country="Brazil")
db.session.add(u66)
u67 = User(
        username="MichaelHolz", customername="Richter Supermarkt", lastname=None, middlename=None,
        firstname="Michael", email="RichterSupermarkt@example.com", address="Grenzacherweg 237", city="Genève", postalcode="1203",
        country="Switzerland")
db.session.add(u67)
u68 = User(
        username="AlejandraCamino", customername="Romero y tomillo", lastname=None, middlename=None,
        firstname="Alejandra", email="Romeroytomillo@example.com", address="Gran Vía, 1", city="Madrid", postalcode="28001",
        country="Spain")
db.session.add(u68)
u69 = User(
        username="JonasBergulfsen", customername="Santé Gourmet", lastname=None, middlename=None,
        firstname="Jonas", email="SantéGourmet@example.com", address="Erling Skakkes gate 78", city="Stavern", postalcode="4110",
        country="Norway")
db.session.add(u69)
u70 = User(
        username="JosePavarotti", customername="Save-a-lot Markets", lastname=None, middlename=None,
        firstname="Jose", email="Save-a-lotMarkets@example.com", address="187 Suffolk Ln.", city="Boise", postalcode="83720",
        country="USA")
db.session.add(u70)
u71 = User(
        username="HariKumar", customername="Seven Seas Imports", lastname=None, middlename=None,
        firstname="Hari", email="SevenSeasImports@example.com", address="90 Wadhurst Rd.", city="London", postalcode="OX15 4NB",
        country="UK")
db.session.add(u71)
u72 = User(
        username="JyttePetersen", customername="Simons bistro", lastname=None, middlename=None,
        firstname="Jytte", email="Simonsbistro@example.com", address="Vinbæltet 34", city="København", postalcode="1734",
        country="Denmark")
db.session.add(u72)
u73 = User(
        username="DominiquePerrier", customername="Spécialités du monde", lastname=None, middlename=None,
        firstname="Dominique", email="Spécialitésdumonde@example.com", address="25, rue Lauriston", city="Paris", postalcode="75016",
        country="France")
db.session.add(u73)
u74 = User(
        username="ArtBraunschweiger", customername="Split Rail Beer & Ale", lastname=None, middlename=None,
        firstname="Art", email="SplitRailBeer&Ale@example.com", address="P.O. Box 555", city="Lander", postalcode="82520",
        country="USA")
db.session.add(u74)
u75 = User(
        username="PascaleCartrain", customername="Suprêmes délices", lastname=None, middlename=None,
        firstname="Pascale", email="Suprêmesdélices@example.com", address="Boulevard Tirou, 255", city="Charleroi", postalcode="B-6000",
        country="Belgium")
db.session.add(u75)
u76 = User(
        username="LizNixon", customername="The Big Cheese", lastname=None, middlename=None,
        firstname="Liz", email="TheBigCheese@example.com", address="89 Jefferson Way Suite 2", city="Portland", postalcode="97201",
        country="USA")
db.session.add(u76)
u77 = User(
        username="LiuWong", customername="The Cracker Box", lastname=None, middlename=None,
        firstname="Liu", email="TheCrackerBox@example.com", address="55 Grizzly Peak Rd.", city="Butte", postalcode="59801",
        country="USA")
db.session.add(u77)
u78 = User(
        username="KarinJosephs", customername="Toms Spezialitäten", lastname=None, middlename=None,
        firstname="Karin", email="TomsSpezialitäten@example.com", address="Luisenstr. 48", city="Münster", postalcode="44087",
        country="Germany")
db.session.add(u78)
u79 = User(
        username="MiguelAngelPaolino", customername="Tortuga Restaurante", lastname="Paolino", middlename="Angel",
        firstname="Miguel", email="TortugaRestaurante@example.com", address="Avda. Azteca 123", city="México D.F.", postalcode="05033",
        country="Mexico")
db.session.add(u79)
u80 = User(
        username="AnabelaDomingues", customername="Tradição Hipermercados", lastname=None, middlename=None,
        firstname="Anabela", email="TradiçãoHipermercados@example.com", address="Av. Inês de Castro, 414", city="São Paulo", postalcode="05634-030",
        country="Brazil")
db.session.add(u80)
u81 = User(
        username="HelvetiusNagy", customername="Trail's Head Gourmet Provisioners", lastname=None, middlename=None,
        firstname="Helvetius", email="Trail'sHeadGourmetProvisioners@example.com", address="722 DaVinci Blvd.", city="Kirkland", postalcode="98034",
        country="USA")
db.session.add(u81)
u82 = User(
        username="PalleIbsen", customername="Vaffeljernet", lastname=None, middlename=None,
        firstname="Palle", email="Vaffeljernet@example.com", address="Smagsløget 45", city="Århus", postalcode="8200",
        country="Denmark")
db.session.add(u82)
u83 = User(
        username="MarySaveley", customername="Victuailles en stock", lastname=None, middlename=None,
        firstname="Mary", email="Victuaillesenstock@example.com", address="2, rue du Commerce", city="Lyon", postalcode="69004",
        country="France")
db.session.add(u83)
u84 = User(
        username="PaulHenriot", customername="Vins et alcools Chevalier", lastname=None, middlename=None,
        firstname="Paul", email="VinsetalcoolsChevalier@example.com", address="59 rue de l'Abbaye", city="Reims", postalcode="51100",
        country="France")
db.session.add(u84)
u85 = User(
        username="RitaMüller", customername="Die Wandernde Kuh", lastname=None, middlename=None,
        firstname="Rita", email="DieWanderndeKuh@example.com", address="Adenauerallee 900", city="Stuttgart", postalcode="70563",
        country="Germany")
db.session.add(u85)
u86 = User(
        username="PirkkoKoskitalo", customername="Wartian Herkku", lastname=None, middlename=None,
        firstname="Pirkko", email="WartianHerkku@example.com", address="Torikatu 38", city="Oulu", postalcode="90110",
        country="Finland")
db.session.add(u86)
u87 = User(
        username="PaulaParente", customername="Wellington Importadora", lastname=None, middlename=None,
        firstname="Paula", email="WellingtonImportadora@example.com", address="Rua do Mercado, 12", city="Resende", postalcode="08737-363",
        country="Brazil")
db.session.add(u87)
u88 = User(
        username="KarlJablonski", customername="White Clover Markets", lastname=None, middlename=None,
        firstname="Karl", email="WhiteCloverMarkets@example.com", address="305 - 14th Ave. S. Suite 3B", city="Seattle", postalcode="98128",
        country="USA")
db.session.add(u88)
u89 = User(
        username="MattiKarttunen", customername="Wilman Kala", lastname=None, middlename=None,
        firstname="Matti", email="WilmanKala@example.com", address="Keskuskatu 45", city="Helsinki", postalcode="21240",
        country="Finland")
db.session.add(u89)
u90 = User(
        username="Zbyszek", customername="Wolski", lastname=None, middlename=None,
        firstname="Zbyszek", email="Wolski@example.com", address="ul. Filtrowa 68", city="Walla", postalcode="01-012",
        country="Poland")
db.session.add(u90)
db.session.commit()
print('User data added!')






su1 = Supplier(suppliername="Exotic Liquid", contactname="Charlotte Cooper", address="49 Gilbert St.", city="Londona", postalcode="EC1 4SD", country="UK", phone="(171) 555-2222")
db.session.add(su1)
su2 = Supplier(suppliername="New Orleans Cajun Delights", contactname="Shelley Burke", address="P.O. Box 78934", city="New Orleans", postalcode="70117", country="USA", phone="(100) 555-4822")
db.session.add(su2)
su3 = Supplier(suppliername="Grandma Kelly's Homestead", contactname="Regina Murphy", address="707 Oxford Rd.", city="Ann Arbor", postalcode="48104", country="USA", phone="(313) 555-5735")
db.session.add(su3)
su4 = Supplier(suppliername="Tokyo Traders", contactname="Yoshi Nagase", address="9-8 Sekimai Musashino-shi", city="Tokyo", postalcode="100", country="Japan", phone="(03) 3555-5011")
db.session.add(su4)
su5 = Supplier(suppliername="Cooperativa de Quesos 'Las Cabras'", contactname="Antonio del Valle Saavedra ", address="Calle del Rosal 4", city="Oviedo", postalcode="33007", country="Spain", phone="(98) 598 76 54")
db.session.add(su5)
su6 = Supplier(suppliername="Mayumi's", contactname="Mayumi Ohno", address="92 Setsuko Chuo-ku", city="Osaka", postalcode="545", country="Japan", phone="(06) 431-7877")
db.session.add(su6)
su7 = Supplier(suppliername="Pavlova, Ltd.", contactname="Ian Devling", address="74 Rose St. Moonie Ponds", city="Melbourne", postalcode="3058", country="Australia", phone="(03) 444-2343")
db.session.add(su7)
su8 = Supplier(suppliername="Specialty Biscuits, Ltd.", contactname="Peter Wilson", address="29 King's Way", city="Manchester", postalcode="M14 GSD", country="UK", phone="(161) 555-4448")
db.session.add(su8)
su9 = Supplier(suppliername="PB Knäckebröd AB", contactname="Lars Peterson", address="Kaloadagatan 13", city="Göteborg", postalcode="S-345 67", country="Sweden ", phone="031-987 65 43")
db.session.add(su9)
su10 = Supplier(suppliername="Refrescos Americanas LTDA", contactname="Carlos Diaz", address="Av. das Americanas 12.890", city="São Paulo", postalcode="5442", country="Brazil", phone="(11) 555 4640")
db.session.add(su10)
su11 = Supplier(suppliername="Heli Süßwaren GmbH &amp; Co. KG", contactname="Petra Winkler", address="Tiergartenstraße 5", city="Berlin", postalcode="10785", country="Germany", phone="(010) 9984510")
db.session.add(su11)
su12 = Supplier(suppliername="Plutzer Lebensmittelgroßmärkte AG", contactname="Martin Bein", address="Bogenallee 51", city="Frankfurt", postalcode="60439", country="Germany", phone="(069) 992755")
db.session.add(su12)
su13 = Supplier(suppliername="Nord-Ost-Fisch Handelsgesellschaft mbH", contactname="Sven Petersen", address="Frahmredder 112a", city="Cuxhaven", postalcode="27478", country="Germany", phone="(04721) 8713")
db.session.add(su13)
su14 = Supplier(suppliername="Formaggi Fortini s.r.l.", contactname="Elio Rossi", address="Viale Dante, 75", city="Ravenna", postalcode="48100", country="Italy", phone="(0544) 60323")
db.session.add(su14)
su15 = Supplier(suppliername="Norske Meierier", contactname="Beate Vileid", address="Hatlevegen 5", city="Sandvika", postalcode="1320", country="Norway", phone="(0)2-953010")
db.session.add(su15)
su16 = Supplier(suppliername="Bigfoot Breweries", contactname="Cheryl Saylor", address="3400 - 8th Avenue Suite 210", city="Bend", postalcode="97101", country="USA", phone="(503) 555-9931")
db.session.add(su16)
su17 = Supplier(suppliername="Svensk Sjöföda AB", contactname="Michael Björn", address="Brovallavägen 231", city="Stockholm", postalcode="S-123 45", country="Sweden", phone="08-123 45 67")
db.session.add(su17)
su18 = Supplier(suppliername="Aux joyeux ecclésiastiques", contactname="Guylène Nodier", address="203, Rue des Francs-Bourgeois", city="Paris", postalcode="75004", country="France", phone="(1) 03.83.00.68")
db.session.add(su18)
su19 = Supplier(suppliername="New England Seafood Cannery", contactname="Robb Merchant", address="Order Processing Dept. 2100 Paul Revere Blvd.", city="Boston", postalcode="02134", country="USA", phone="(617) 555-3267")
db.session.add(su19)
su20 = Supplier(suppliername="Leka Trading", contactname="Chandra Leka", address="471 Serangoon Loop, Suite #402", city="Singapore", postalcode="0512", country="Singapore", phone="555-8787")
db.session.add(su20)
su21 = Supplier(suppliername="Lyngbysild", contactname="Niels Petersen", address="Lyngbysild Fiskebakken 10", city="Lyngby", postalcode="2800", country="Denmark", phone="43844108")
db.session.add(su21)
su22 = Supplier(suppliername="Zaanse Snoepfabriek", contactname="Dirk Luchte", address="Verkoop Rijnweg 22", city="Zaandam", postalcode="9999 ZZ", country="Netherlands", phone="(12345) 1212")
db.session.add(su22)
su23 = Supplier(suppliername="Karkki Oy", contactname="Anne Heikkonen", address="Valtakatu 12", city="Lappeenranta", postalcode="53120", country="Finland", phone="(953) 10956")
db.session.add(su23)
su24 = Supplier(suppliername="G'day, Mate", contactname="Wendy Mackenzie", address="170 Prince Edward Parade Hunter's Hill", city="Sydney", postalcode="2042", country="Australia", phone="(02) 555-5914")
db.session.add(su24)
su25 = Supplier(suppliername="Ma Maison", contactname="Jean-Guy Lauzon", address="2960 Rue St. Laurent", city="Montréal", postalcode="H1J 1C3", country="Canada", phone="(514) 555-9022")
db.session.add(su25)
su26 = Supplier(suppliername="Pasta Buttini s.r.l.", contactname="Giovanni Giudici", address="Via dei Gelsomini, 153", city="Salerno", postalcode="84100", country="Italy", phone="(089) 6547665")
db.session.add(su26)
su27 = Supplier(suppliername="Escargots Nouveaux", contactname="Marie Delamare", address="22, rue H. Voiron", city="Montceau", postalcode="71300", country="France", phone="85.57.00.07")
db.session.add(su27)
su28 = Supplier(suppliername="Gai pâturage", contactname="Eliane Noz", address="Bat. B 3, rue des Alpes", city="Annecy", postalcode="74000", country="France", phone="38.76.98.06")
db.session.add(su28)
su29 = Supplier(suppliername="Forêts d'érables", contactname="Chantal Goulet", address="148 rue Chasseur", city="Ste-Hyacinthe", postalcode="J2S 7S8", country="Canada", phone="(514) 555-2955")
db.session.add(su29)
db.session.commit()
print('Supplier data added!')






e0 = Employee(lastname="Davolio", firstname="Nancy", notes="Education includes a BA in psychology from Colorado State University. She also completed (The Art of the Cold Call). Nancy is a member of 'Toastmasters International'.")
db.session.add(e0)
e1 = Employee(lastname="Fuller", firstname="Andrew", notes="Andrew received his BTS commercial and a Ph.D. in international marketing from the University of Dallas. He is fluent in French and Italian and reads German. He joined the company as a sales representative, was promoted to sales manager and was then named vice president of sales. Andrew is a member of the Sales Management Roundtable, the Seattle Chamber of Commerce, and the Pacific Rim Importers Association.")
db.session.add(e1)
e2 = Employee(lastname="Leverling", firstname="Janet", notes="Janet has a BS degree in chemistry from Boston College). She has also completed a certificate program in food retailing management. Janet was hired as a sales associate and was promoted to sales representative.")
db.session.add(e2)
e3 = Employee(lastname="Peacock", firstname="Margaret", notes="Margaret holds a BA in English literature from Concordia College and an MA from the American Institute of Culinary Arts. She was temporarily assigned to the London office before returning to her permanent post in Seattle.")
db.session.add(e3)
e4 = Employee(lastname="Buchanan", firstname="Steven", notes="Steven Buchanan graduated from St. Andrews University, Scotland, with a BSC degree. Upon joining the company as a sales representative, he spent 6 months in an orientation program at the Seattle office and then returned to his permanent post in London, where he was promoted to sales manager. Mr. Buchanan has completed the courses 'Successful Telemarketing' and 'International Sales Management'. He is fluent in French.")
db.session.add(e4)
e5 = Employee(lastname="Suyama", firstname="Michael", notes="Michael is a graduate of Sussex University (MA, economics) and the University of California at Los Angeles (MBA, marketing). He has also taken the courses 'Multi-Cultural Selling' and 'Time Management for the Sales Professional'. He is fluent in Japanese and can read and write French, Portuguese, and Spanish.")
db.session.add(e5)
e6 = Employee(lastname="King", firstname="Robert", notes="Robert King served in the Peace Corps and traveled extensively before completing his degree in English at the University of Michigan and then joining the company. After completing a course entitled 'Selling in Europe', he was transferred to the London office.")
db.session.add(e6)
e7 = Employee(lastname="Callahan", firstname="Laura", notes="Laura received a BA in psychology from the University of Washington. She has also completed a course in business French. She reads and writes French.")
db.session.add(e7)
e8 = Employee(lastname="Dodsworth", firstname="Anne", notes="Anne has a BA degree in English from St. Lawrence College. She is fluent in French and German.")
db.session.add(e8)
e9 = Employee(lastname="West", firstname="Adam", notes="An old chum.")
db.session.add(e9)
db.session.commit()
print('Employee data added!')






c0 = Category(categoryname="Soft drinks, coffees, teas, beers, and ales", description="Beverages")
db.session.add(c0)
c1 = Category(categoryname="Sweet and savory sauces, relishes, spreads, and seasonings", description="Condiments")
db.session.add(c1)
c2 = Category(categoryname="Desserts, candies, and sweet breads", description="Confections")
db.session.add(c2)
c3 = Category(categoryname="Cheeses", description="Dairy Products")
db.session.add(c3)
c4 = Category(categoryname="Breads, crackers, pasta, and cereal", description="Grains/Cereals")
db.session.add(c4)
c5 = Category(categoryname="Prepared meats", description="Meat/Poultry")
db.session.add(c5)
c6 = Category(categoryname="Dried fruit and bean curd", description="Produce")
db.session.add(c6)
c7 = Category(categoryname="Seaweed and fish", description="Seafood")
db.session.add(c7)
db.session.commit()
print('Category data added!')






s1 = Shipper(shippername="Speedy Express", phone="(503) 555-9831")
db.session.add(s1)
s2 = Shipper(shippername="United Package", phone="(503) 555-3199")
db.session.add(s2)
s3 = Shipper(shippername="Federal Shipping", phone="(503) 555-9931")
db.session.add(s3)
db.session.commit()
print('Shipper data added!')
