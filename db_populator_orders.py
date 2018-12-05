from datetime import datetime
from app import db
from app.models import User, Order, Shipper



user = User.query.get(int(90))
shipper = Shipper.query.get(int(3))
o10248 = Order(id=10248, customer=user, orderdate=datetime(1996, 7, 4), shipper=shipper)
db.session.add(o10248)

user = User.query.get(int(81))
shipper = Shipper.query.get(int(1))
o10249 = Order(id=10249, customer=user, orderdate=datetime(1996, 7, 5), shipper=shipper)
db.session.add(o10249)

user = User.query.get(int(34))
shipper = Shipper.query.get(int(2))
o10250 = Order(id=10250, customer=user, orderdate=datetime(1996, 7, 8), shipper=shipper)
db.session.add(o10250)

user = User.query.get(int(84))
shipper = Shipper.query.get(int(1))
o10251 = Order(id=10251, customer=user, orderdate=datetime(1996, 7, 8), shipper=shipper)
db.session.add(o10251)

user = User.query.get(int(76))
shipper = Shipper.query.get(int(2))
o10252 = Order(id=10252, customer=user, orderdate=datetime(1996, 7, 9), shipper=shipper)
db.session.add(o10252)

user = User.query.get(int(34))
shipper = Shipper.query.get(int(2))
o10253 = Order(id=10253, customer=user, orderdate=datetime(1996, 7, 10), shipper=shipper)
db.session.add(o10253)

user = User.query.get(int(14))
shipper = Shipper.query.get(int(2))
o10254 = Order(id=10254, customer=user, orderdate=datetime(1996, 7, 11), shipper=shipper)
db.session.add(o10254)

user = User.query.get(int(68))
shipper = Shipper.query.get(int(3))
o10255 = Order(id=10255, customer=user, orderdate=datetime(1996, 7, 12), shipper=shipper)
db.session.add(o10255)

user = User.query.get(int(88))
shipper = Shipper.query.get(int(2))
o10256 = Order(id=10256, customer=user, orderdate=datetime(1996, 7, 15), shipper=shipper)
db.session.add(o10256)

user = User.query.get(int(35))
shipper = Shipper.query.get(int(3))
o10257 = Order(id=10257, customer=user, orderdate=datetime(1996, 7, 16), shipper=shipper)
db.session.add(o10257)

user = User.query.get(int(20))
shipper = Shipper.query.get(int(1))
o10258 = Order(id=10258, customer=user, orderdate=datetime(1996, 7, 17), shipper=shipper)
db.session.add(o10258)

user = User.query.get(int(13))
shipper = Shipper.query.get(int(3))
o10259 = Order(id=10259, customer=user, orderdate=datetime(1996, 7, 18), shipper=shipper)
db.session.add(o10259)

user = User.query.get(int(55))
shipper = Shipper.query.get(int(1))
o10260 = Order(id=10260, customer=user, orderdate=datetime(1996, 7, 19), shipper=shipper)
db.session.add(o10260)

user = User.query.get(int(61))
shipper = Shipper.query.get(int(2))
o10261 = Order(id=10261, customer=user, orderdate=datetime(1996, 7, 19), shipper=shipper)
db.session.add(o10261)

user = User.query.get(int(65))
shipper = Shipper.query.get(int(3))
o10262 = Order(id=10262, customer=user, orderdate=datetime(1996, 7, 22), shipper=shipper)
db.session.add(o10262)

user = User.query.get(int(20))
shipper = Shipper.query.get(int(3))
o10263 = Order(id=10263, customer=user, orderdate=datetime(1996, 7, 23), shipper=shipper)
db.session.add(o10263)

user = User.query.get(int(24))
shipper = Shipper.query.get(int(3))
o10264 = Order(id=10264, customer=user, orderdate=datetime(1996, 7, 24), shipper=shipper)
db.session.add(o10264)

user = User.query.get(int(7))
shipper = Shipper.query.get(int(1))
o10265 = Order(id=10265, customer=user, orderdate=datetime(1996, 7, 25), shipper=shipper)
db.session.add(o10265)

user = User.query.get(int(87))
shipper = Shipper.query.get(int(3))
o10266 = Order(id=10266, customer=user, orderdate=datetime(1996, 7, 26), shipper=shipper)
db.session.add(o10266)

user = User.query.get(int(25))
shipper = Shipper.query.get(int(1))
o10267 = Order(id=10267, customer=user, orderdate=datetime(1996, 7, 29), shipper=shipper)
db.session.add(o10267)

user = User.query.get(int(33))
shipper = Shipper.query.get(int(3))
o10268 = Order(id=10268, customer=user, orderdate=datetime(1996, 7, 30), shipper=shipper)
db.session.add(o10268)

user = User.query.get(int(89))
shipper = Shipper.query.get(int(1))
o10269 = Order(id=10269, customer=user, orderdate=datetime(1996, 7, 31), shipper=shipper)
db.session.add(o10269)

user = User.query.get(int(87))
shipper = Shipper.query.get(int(1))
o10270 = Order(id=10270, customer=user, orderdate=datetime(1996, 8, 1), shipper=shipper)
db.session.add(o10270)

user = User.query.get(int(75))
shipper = Shipper.query.get(int(2))
o10271 = Order(id=10271, customer=user, orderdate=datetime(1996, 8, 1), shipper=shipper)
db.session.add(o10271)

user = User.query.get(int(65))
shipper = Shipper.query.get(int(2))
o10272 = Order(id=10272, customer=user, orderdate=datetime(1996, 8, 2), shipper=shipper)
db.session.add(o10272)

user = User.query.get(int(63))
shipper = Shipper.query.get(int(3))
o10273 = Order(id=10273, customer=user, orderdate=datetime(1996, 8, 5), shipper=shipper)
db.session.add(o10273)

user = User.query.get(int(85))
shipper = Shipper.query.get(int(1))
o10274 = Order(id=10274, customer=user, orderdate=datetime(1996, 8, 6), shipper=shipper)
db.session.add(o10274)

user = User.query.get(int(49))
shipper = Shipper.query.get(int(1))
o10275 = Order(id=10275, customer=user, orderdate=datetime(1996, 8, 7), shipper=shipper)
db.session.add(o10275)

user = User.query.get(int(80))
shipper = Shipper.query.get(int(3))
o10276 = Order(id=10276, customer=user, orderdate=datetime(1996, 8, 8), shipper=shipper)
db.session.add(o10276)

user = User.query.get(int(52))
shipper = Shipper.query.get(int(3))
o10277 = Order(id=10277, customer=user, orderdate=datetime(1996, 8, 9), shipper=shipper)
db.session.add(o10277)

user = User.query.get(int(5))
shipper = Shipper.query.get(int(2))
o10278 = Order(id=10278, customer=user, orderdate=datetime(1996, 8, 12), shipper=shipper)
db.session.add(o10278)

user = User.query.get(int(44))
shipper = Shipper.query.get(int(2))
o10279 = Order(id=10279, customer=user, orderdate=datetime(1996, 8, 13), shipper=shipper)
db.session.add(o10279)

user = User.query.get(int(5))
shipper = Shipper.query.get(int(1))
o10280 = Order(id=10280, customer=user, orderdate=datetime(1996, 8, 14), shipper=shipper)
db.session.add(o10280)

user = User.query.get(int(69))
shipper = Shipper.query.get(int(1))
o10281 = Order(id=10281, customer=user, orderdate=datetime(1996, 8, 14), shipper=shipper)
db.session.add(o10281)

user = User.query.get(int(69))
shipper = Shipper.query.get(int(1))
o10282 = Order(id=10282, customer=user, orderdate=datetime(1996, 8, 15), shipper=shipper)
db.session.add(o10282)

user = User.query.get(int(46))
shipper = Shipper.query.get(int(3))
o10283 = Order(id=10283, customer=user, orderdate=datetime(1996, 8, 16), shipper=shipper)
db.session.add(o10283)

user = User.query.get(int(44))
shipper = Shipper.query.get(int(1))
o10284 = Order(id=10284, customer=user, orderdate=datetime(1996, 8, 19), shipper=shipper)
db.session.add(o10284)

user = User.query.get(int(63))
shipper = Shipper.query.get(int(2))
o10285 = Order(id=10285, customer=user, orderdate=datetime(1996, 8, 20), shipper=shipper)
db.session.add(o10285)

user = User.query.get(int(63))
shipper = Shipper.query.get(int(3))
o10286 = Order(id=10286, customer=user, orderdate=datetime(1996, 8, 21), shipper=shipper)
db.session.add(o10286)

user = User.query.get(int(67))
shipper = Shipper.query.get(int(3))
o10287 = Order(id=10287, customer=user, orderdate=datetime(1996, 8, 22), shipper=shipper)
db.session.add(o10287)

user = User.query.get(int(66))
shipper = Shipper.query.get(int(1))
o10288 = Order(id=10288, customer=user, orderdate=datetime(1996, 8, 23), shipper=shipper)
db.session.add(o10288)

user = User.query.get(int(11))
shipper = Shipper.query.get(int(3))
o10289 = Order(id=10289, customer=user, orderdate=datetime(1996, 8, 26), shipper=shipper)
db.session.add(o10289)

user = User.query.get(int(15))
shipper = Shipper.query.get(int(1))
o10290 = Order(id=10290, customer=user, orderdate=datetime(1996, 8, 27), shipper=shipper)
db.session.add(o10290)

user = User.query.get(int(61))
shipper = Shipper.query.get(int(2))
o10291 = Order(id=10291, customer=user, orderdate=datetime(1996, 8, 27), shipper=shipper)
db.session.add(o10291)

user = User.query.get(int(81))
shipper = Shipper.query.get(int(2))
o10292 = Order(id=10292, customer=user, orderdate=datetime(1996, 8, 28), shipper=shipper)
db.session.add(o10292)

user = User.query.get(int(80))
shipper = Shipper.query.get(int(3))
o10293 = Order(id=10293, customer=user, orderdate=datetime(1996, 8, 29), shipper=shipper)
db.session.add(o10293)

user = User.query.get(int(65))
shipper = Shipper.query.get(int(2))
o10294 = Order(id=10294, customer=user, orderdate=datetime(1996, 8, 30), shipper=shipper)
db.session.add(o10294)

user = User.query.get(int(85))
shipper = Shipper.query.get(int(2))
o10295 = Order(id=10295, customer=user, orderdate=datetime(1996, 9, 2), shipper=shipper)
db.session.add(o10295)

user = User.query.get(int(46))
shipper = Shipper.query.get(int(1))
o10296 = Order(id=10296, customer=user, orderdate=datetime(1996, 9, 3), shipper=shipper)
db.session.add(o10296)

user = User.query.get(int(7))
shipper = Shipper.query.get(int(2))
o10297 = Order(id=10297, customer=user, orderdate=datetime(1996, 9, 4), shipper=shipper)
db.session.add(o10297)

user = User.query.get(int(37))
shipper = Shipper.query.get(int(2))
o10298 = Order(id=10298, customer=user, orderdate=datetime(1996, 9, 5), shipper=shipper)
db.session.add(o10298)

user = User.query.get(int(67))
shipper = Shipper.query.get(int(2))
o10299 = Order(id=10299, customer=user, orderdate=datetime(1996, 9, 6), shipper=shipper)
db.session.add(o10299)

user = User.query.get(int(49))
shipper = Shipper.query.get(int(2))
o10300 = Order(id=10300, customer=user, orderdate=datetime(1996, 9, 9), shipper=shipper)
db.session.add(o10300)

user = User.query.get(int(86))
shipper = Shipper.query.get(int(2))
o10301 = Order(id=10301, customer=user, orderdate=datetime(1996, 9, 9), shipper=shipper)
db.session.add(o10301)

user = User.query.get(int(76))
shipper = Shipper.query.get(int(2))
o10302 = Order(id=10302, customer=user, orderdate=datetime(1996, 9, 10), shipper=shipper)
db.session.add(o10302)

user = User.query.get(int(30))
shipper = Shipper.query.get(int(2))
o10303 = Order(id=10303, customer=user, orderdate=datetime(1996, 9, 11), shipper=shipper)
db.session.add(o10303)

user = User.query.get(int(80))
shipper = Shipper.query.get(int(2))
o10304 = Order(id=10304, customer=user, orderdate=datetime(1996, 9, 12), shipper=shipper)
db.session.add(o10304)

user = User.query.get(int(55))
shipper = Shipper.query.get(int(3))
o10305 = Order(id=10305, customer=user, orderdate=datetime(1996, 9, 13), shipper=shipper)
db.session.add(o10305)

user = User.query.get(int(69))
shipper = Shipper.query.get(int(3))
o10306 = Order(id=10306, customer=user, orderdate=datetime(1996, 9, 16), shipper=shipper)
db.session.add(o10306)

user = User.query.get(int(48))
shipper = Shipper.query.get(int(2))
o10307 = Order(id=10307, customer=user, orderdate=datetime(1996, 9, 17), shipper=shipper)
db.session.add(o10307)

user = User.query.get(int(2))
shipper = Shipper.query.get(int(3))
o10308 = Order(id=10308, customer=user, orderdate=datetime(1996, 9, 18), shipper=shipper)
db.session.add(o10308)

user = User.query.get(int(37))
shipper = Shipper.query.get(int(1))
o10309 = Order(id=10309, customer=user, orderdate=datetime(1996, 9, 19), shipper=shipper)
db.session.add(o10309)

user = User.query.get(int(77))
shipper = Shipper.query.get(int(2))
o10310 = Order(id=10310, customer=user, orderdate=datetime(1996, 9, 20), shipper=shipper)
db.session.add(o10310)

user = User.query.get(int(18))
shipper = Shipper.query.get(int(3))
o10311 = Order(id=10311, customer=user, orderdate=datetime(1996, 9, 20), shipper=shipper)
db.session.add(o10311)

user = User.query.get(int(86))
shipper = Shipper.query.get(int(2))
o10312 = Order(id=10312, customer=user, orderdate=datetime(1996, 9, 23), shipper=shipper)
db.session.add(o10312)

user = User.query.get(int(63))
shipper = Shipper.query.get(int(2))
o10313 = Order(id=10313, customer=user, orderdate=datetime(1996, 9, 24), shipper=shipper)
db.session.add(o10313)

user = User.query.get(int(65))
shipper = Shipper.query.get(int(2))
o10314 = Order(id=10314, customer=user, orderdate=datetime(1996, 9, 25), shipper=shipper)
db.session.add(o10314)

user = User.query.get(int(38))
shipper = Shipper.query.get(int(2))
o10315 = Order(id=10315, customer=user, orderdate=datetime(1996, 9, 26), shipper=shipper)
db.session.add(o10315)

user = User.query.get(int(65))
shipper = Shipper.query.get(int(3))
o10316 = Order(id=10316, customer=user, orderdate=datetime(1996, 9, 27), shipper=shipper)
db.session.add(o10316)

user = User.query.get(int(48))
shipper = Shipper.query.get(int(1))
o10317 = Order(id=10317, customer=user, orderdate=datetime(1996, 9, 30), shipper=shipper)
db.session.add(o10317)

user = User.query.get(int(38))
shipper = Shipper.query.get(int(2))
o10318 = Order(id=10318, customer=user, orderdate=datetime(1996, 10, 1), shipper=shipper)
db.session.add(o10318)

user = User.query.get(int(80))
shipper = Shipper.query.get(int(3))
o10319 = Order(id=10319, customer=user, orderdate=datetime(1996, 10, 2), shipper=shipper)
db.session.add(o10319)

user = User.query.get(int(87))
shipper = Shipper.query.get(int(3))
o10320 = Order(id=10320, customer=user, orderdate=datetime(1996, 10, 3), shipper=shipper)
db.session.add(o10320)

user = User.query.get(int(38))
shipper = Shipper.query.get(int(2))
o10321 = Order(id=10321, customer=user, orderdate=datetime(1996, 10, 3), shipper=shipper)
db.session.add(o10321)

user = User.query.get(int(58))
shipper = Shipper.query.get(int(3))
o10322 = Order(id=10322, customer=user, orderdate=datetime(1996, 10, 4), shipper=shipper)
db.session.add(o10322)

user = User.query.get(int(39))
shipper = Shipper.query.get(int(1))
o10323 = Order(id=10323, customer=user, orderdate=datetime(1996, 10, 7), shipper=shipper)
db.session.add(o10323)

user = User.query.get(int(71))
shipper = Shipper.query.get(int(1))
o10324 = Order(id=10324, customer=user, orderdate=datetime(1996, 10, 8), shipper=shipper)
db.session.add(o10324)

user = User.query.get(int(39))
shipper = Shipper.query.get(int(3))
o10325 = Order(id=10325, customer=user, orderdate=datetime(1996, 10, 9), shipper=shipper)
db.session.add(o10325)

user = User.query.get(int(8))
shipper = Shipper.query.get(int(2))
o10326 = Order(id=10326, customer=user, orderdate=datetime(1996, 10, 10), shipper=shipper)
db.session.add(o10326)

user = User.query.get(int(24))
shipper = Shipper.query.get(int(1))
o10327 = Order(id=10327, customer=user, orderdate=datetime(1996, 10, 11), shipper=shipper)
db.session.add(o10327)

user = User.query.get(int(28))
shipper = Shipper.query.get(int(3))
o10328 = Order(id=10328, customer=user, orderdate=datetime(1996, 10, 14), shipper=shipper)
db.session.add(o10328)

user = User.query.get(int(75))
shipper = Shipper.query.get(int(2))
o10329 = Order(id=10329, customer=user, orderdate=datetime(1996, 10, 15), shipper=shipper)
db.session.add(o10329)

user = User.query.get(int(46))
shipper = Shipper.query.get(int(1))
o10330 = Order(id=10330, customer=user, orderdate=datetime(1996, 10, 16), shipper=shipper)
db.session.add(o10330)

user = User.query.get(int(9))
shipper = Shipper.query.get(int(1))
o10331 = Order(id=10331, customer=user, orderdate=datetime(1996, 10, 16), shipper=shipper)
db.session.add(o10331)

user = User.query.get(int(51))
shipper = Shipper.query.get(int(2))
o10332 = Order(id=10332, customer=user, orderdate=datetime(1996, 10, 17), shipper=shipper)
db.session.add(o10332)

user = User.query.get(int(87))
shipper = Shipper.query.get(int(3))
o10333 = Order(id=10333, customer=user, orderdate=datetime(1996, 10, 18), shipper=shipper)
db.session.add(o10333)

user = User.query.get(int(84))
shipper = Shipper.query.get(int(2))
o10334 = Order(id=10334, customer=user, orderdate=datetime(1996, 10, 21), shipper=shipper)
db.session.add(o10334)

user = User.query.get(int(37))
shipper = Shipper.query.get(int(2))
o10335 = Order(id=10335, customer=user, orderdate=datetime(1996, 10, 22), shipper=shipper)
db.session.add(o10335)

user = User.query.get(int(60))
shipper = Shipper.query.get(int(2))
o10336 = Order(id=10336, customer=user, orderdate=datetime(1996, 10, 23), shipper=shipper)
db.session.add(o10336)

user = User.query.get(int(25))
shipper = Shipper.query.get(int(3))
o10337 = Order(id=10337, customer=user, orderdate=datetime(1996, 10, 24), shipper=shipper)
db.session.add(o10337)

user = User.query.get(int(55))
shipper = Shipper.query.get(int(3))
o10338 = Order(id=10338, customer=user, orderdate=datetime(1996, 10, 25), shipper=shipper)
db.session.add(o10338)

user = User.query.get(int(51))
shipper = Shipper.query.get(int(2))
o10339 = Order(id=10339, customer=user, orderdate=datetime(1996, 10, 28), shipper=shipper)
db.session.add(o10339)

user = User.query.get(int(9))
shipper = Shipper.query.get(int(3))
o10340 = Order(id=10340, customer=user, orderdate=datetime(1996, 10, 29), shipper=shipper)
db.session.add(o10340)

user = User.query.get(int(73))
shipper = Shipper.query.get(int(3))
o10341 = Order(id=10341, customer=user, orderdate=datetime(1996, 10, 29), shipper=shipper)
db.session.add(o10341)

user = User.query.get(int(25))
shipper = Shipper.query.get(int(2))
o10342 = Order(id=10342, customer=user, orderdate=datetime(1996, 10, 30), shipper=shipper)
db.session.add(o10342)

user = User.query.get(int(44))
shipper = Shipper.query.get(int(1))
o10343 = Order(id=10343, customer=user, orderdate=datetime(1996, 10, 31), shipper=shipper)
db.session.add(o10343)

user = User.query.get(int(89))
shipper = Shipper.query.get(int(2))
o10344 = Order(id=10344, customer=user, orderdate=datetime(1996, 11, 1), shipper=shipper)
db.session.add(o10344)

user = User.query.get(int(63))
shipper = Shipper.query.get(int(2))
o10345 = Order(id=10345, customer=user, orderdate=datetime(1996, 11, 4), shipper=shipper)
db.session.add(o10345)

user = User.query.get(int(65))
shipper = Shipper.query.get(int(3))
o10346 = Order(id=10346, customer=user, orderdate=datetime(1996, 11, 5), shipper=shipper)
db.session.add(o10346)

user = User.query.get(int(21))
shipper = Shipper.query.get(int(3))
o10347 = Order(id=10347, customer=user, orderdate=datetime(1996, 11, 6), shipper=shipper)
db.session.add(o10347)

user = User.query.get(int(86))
shipper = Shipper.query.get(int(2))
o10348 = Order(id=10348, customer=user, orderdate=datetime(1996, 11, 7), shipper=shipper)
db.session.add(o10348)

user = User.query.get(int(75))
shipper = Shipper.query.get(int(1))
o10349 = Order(id=10349, customer=user, orderdate=datetime(1996, 11, 8), shipper=shipper)
db.session.add(o10349)

user = User.query.get(int(41))
shipper = Shipper.query.get(int(2))
o10350 = Order(id=10350, customer=user, orderdate=datetime(1996, 11, 11), shipper=shipper)
db.session.add(o10350)

user = User.query.get(int(20))
shipper = Shipper.query.get(int(1))
o10351 = Order(id=10351, customer=user, orderdate=datetime(1996, 11, 11), shipper=shipper)
db.session.add(o10351)

user = User.query.get(int(28))
shipper = Shipper.query.get(int(3))
o10352 = Order(id=10352, customer=user, orderdate=datetime(1996, 11, 12), shipper=shipper)
db.session.add(o10352)

user = User.query.get(int(59))
shipper = Shipper.query.get(int(3))
o10353 = Order(id=10353, customer=user, orderdate=datetime(1996, 11, 13), shipper=shipper)
db.session.add(o10353)

user = User.query.get(int(58))
shipper = Shipper.query.get(int(3))
o10354 = Order(id=10354, customer=user, orderdate=datetime(1996, 11, 14), shipper=shipper)
db.session.add(o10354)

user = User.query.get(int(4))
shipper = Shipper.query.get(int(1))
o10355 = Order(id=10355, customer=user, orderdate=datetime(1996, 11, 15), shipper=shipper)
db.session.add(o10355)

user = User.query.get(int(86))
shipper = Shipper.query.get(int(2))
o10356 = Order(id=10356, customer=user, orderdate=datetime(1996, 11, 18), shipper=shipper)
db.session.add(o10356)

user = User.query.get(int(46))
shipper = Shipper.query.get(int(3))
o10357 = Order(id=10357, customer=user, orderdate=datetime(1996, 11, 19), shipper=shipper)
db.session.add(o10357)

user = User.query.get(int(41))
shipper = Shipper.query.get(int(1))
o10358 = Order(id=10358, customer=user, orderdate=datetime(1996, 11, 20), shipper=shipper)
db.session.add(o10358)

user = User.query.get(int(72))
shipper = Shipper.query.get(int(3))
o10359 = Order(id=10359, customer=user, orderdate=datetime(1996, 11, 21), shipper=shipper)
db.session.add(o10359)

user = User.query.get(int(7))
shipper = Shipper.query.get(int(3))
o10360 = Order(id=10360, customer=user, orderdate=datetime(1996, 11, 22), shipper=shipper)
db.session.add(o10360)

user = User.query.get(int(63))
shipper = Shipper.query.get(int(2))
o10361 = Order(id=10361, customer=user, orderdate=datetime(1996, 11, 22), shipper=shipper)
db.session.add(o10361)

user = User.query.get(int(9))
shipper = Shipper.query.get(int(1))
o10362 = Order(id=10362, customer=user, orderdate=datetime(1996, 11, 25), shipper=shipper)
db.session.add(o10362)

user = User.query.get(int(17))
shipper = Shipper.query.get(int(3))
o10363 = Order(id=10363, customer=user, orderdate=datetime(1996, 11, 26), shipper=shipper)
db.session.add(o10363)

user = User.query.get(int(19))
shipper = Shipper.query.get(int(1))
o10364 = Order(id=10364, customer=user, orderdate=datetime(1996, 11, 26), shipper=shipper)
db.session.add(o10364)

user = User.query.get(int(3))
shipper = Shipper.query.get(int(2))
o10365 = Order(id=10365, customer=user, orderdate=datetime(1996, 11, 27), shipper=shipper)
db.session.add(o10365)

user = User.query.get(int(29))
shipper = Shipper.query.get(int(2))
o10366 = Order(id=10366, customer=user, orderdate=datetime(1996, 11, 28), shipper=shipper)
db.session.add(o10366)

user = User.query.get(int(83))
shipper = Shipper.query.get(int(3))
o10367 = Order(id=10367, customer=user, orderdate=datetime(1996, 11, 28), shipper=shipper)
db.session.add(o10367)

user = User.query.get(int(20))
shipper = Shipper.query.get(int(2))
o10368 = Order(id=10368, customer=user, orderdate=datetime(1996, 11, 29), shipper=shipper)
db.session.add(o10368)

user = User.query.get(int(75))
shipper = Shipper.query.get(int(2))
o10369 = Order(id=10369, customer=user, orderdate=datetime(1996, 12, 2), shipper=shipper)
db.session.add(o10369)

user = User.query.get(int(14))
shipper = Shipper.query.get(int(2))
o10370 = Order(id=10370, customer=user, orderdate=datetime(1996, 12, 3), shipper=shipper)
db.session.add(o10370)

user = User.query.get(int(41))
shipper = Shipper.query.get(int(1))
o10371 = Order(id=10371, customer=user, orderdate=datetime(1996, 12, 3), shipper=shipper)
db.session.add(o10371)

user = User.query.get(int(62))
shipper = Shipper.query.get(int(2))
o10372 = Order(id=10372, customer=user, orderdate=datetime(1996, 12, 4), shipper=shipper)
db.session.add(o10372)

user = User.query.get(int(37))
shipper = Shipper.query.get(int(3))
o10373 = Order(id=10373, customer=user, orderdate=datetime(1996, 12, 5), shipper=shipper)
db.session.add(o10373)

user = User.query.get(int(91))
shipper = Shipper.query.get(int(3))
o10374 = Order(id=10374, customer=user, orderdate=datetime(1996, 12, 5), shipper=shipper)
db.session.add(o10374)

user = User.query.get(int(36))
shipper = Shipper.query.get(int(2))
o10375 = Order(id=10375, customer=user, orderdate=datetime(1996, 12, 6), shipper=shipper)
db.session.add(o10375)

user = User.query.get(int(51))
shipper = Shipper.query.get(int(2))
o10376 = Order(id=10376, customer=user, orderdate=datetime(1996, 12, 9), shipper=shipper)
db.session.add(o10376)

user = User.query.get(int(72))
shipper = Shipper.query.get(int(3))
o10377 = Order(id=10377, customer=user, orderdate=datetime(1996, 12, 9), shipper=shipper)
db.session.add(o10377)

user = User.query.get(int(24))
shipper = Shipper.query.get(int(3))
o10378 = Order(id=10378, customer=user, orderdate=datetime(1996, 12, 10), shipper=shipper)
db.session.add(o10378)

user = User.query.get(int(61))
shipper = Shipper.query.get(int(1))
o10379 = Order(id=10379, customer=user, orderdate=datetime(1996, 12, 11), shipper=shipper)
db.session.add(o10379)

user = User.query.get(int(37))
shipper = Shipper.query.get(int(3))
o10380 = Order(id=10380, customer=user, orderdate=datetime(1996, 12, 12), shipper=shipper)
db.session.add(o10380)

user = User.query.get(int(46))
shipper = Shipper.query.get(int(3))
o10381 = Order(id=10381, customer=user, orderdate=datetime(1996, 12, 12), shipper=shipper)
db.session.add(o10381)

user = User.query.get(int(20))
shipper = Shipper.query.get(int(1))
o10382 = Order(id=10382, customer=user, orderdate=datetime(1996, 12, 13), shipper=shipper)
db.session.add(o10382)

user = User.query.get(int(4))
shipper = Shipper.query.get(int(3))
o10383 = Order(id=10383, customer=user, orderdate=datetime(1996, 12, 16), shipper=shipper)
db.session.add(o10383)

user = User.query.get(int(5))
shipper = Shipper.query.get(int(3))
o10384 = Order(id=10384, customer=user, orderdate=datetime(1996, 12, 16), shipper=shipper)
db.session.add(o10384)

user = User.query.get(int(75))
shipper = Shipper.query.get(int(2))
o10385 = Order(id=10385, customer=user, orderdate=datetime(1996, 12, 17), shipper=shipper)
db.session.add(o10385)

user = User.query.get(int(21))
shipper = Shipper.query.get(int(3))
o10386 = Order(id=10386, customer=user, orderdate=datetime(1996, 12, 18), shipper=shipper)
db.session.add(o10386)

user = User.query.get(int(70))
shipper = Shipper.query.get(int(2))
o10387 = Order(id=10387, customer=user, orderdate=datetime(1996, 12, 18), shipper=shipper)
db.session.add(o10387)

user = User.query.get(int(72))
shipper = Shipper.query.get(int(1))
o10388 = Order(id=10388, customer=user, orderdate=datetime(1996, 12, 19), shipper=shipper)
db.session.add(o10388)

user = User.query.get(int(10))
shipper = Shipper.query.get(int(2))
o10389 = Order(id=10389, customer=user, orderdate=datetime(1996, 12, 20), shipper=shipper)
db.session.add(o10389)

user = User.query.get(int(20))
shipper = Shipper.query.get(int(1))
o10390 = Order(id=10390, customer=user, orderdate=datetime(1996, 12, 23), shipper=shipper)
db.session.add(o10390)

user = User.query.get(int(17))
shipper = Shipper.query.get(int(3))
o10391 = Order(id=10391, customer=user, orderdate=datetime(1996, 12, 23), shipper=shipper)
db.session.add(o10391)

user = User.query.get(int(59))
shipper = Shipper.query.get(int(3))
o10392 = Order(id=10392, customer=user, orderdate=datetime(1996, 12, 24), shipper=shipper)
db.session.add(o10392)

user = User.query.get(int(71))
shipper = Shipper.query.get(int(3))
o10393 = Order(id=10393, customer=user, orderdate=datetime(1996, 12, 25), shipper=shipper)
db.session.add(o10393)

user = User.query.get(int(36))
shipper = Shipper.query.get(int(3))
o10394 = Order(id=10394, customer=user, orderdate=datetime(1996, 12, 25), shipper=shipper)
db.session.add(o10394)

user = User.query.get(int(35))
shipper = Shipper.query.get(int(1))
o10395 = Order(id=10395, customer=user, orderdate=datetime(1996, 12, 26), shipper=shipper)
db.session.add(o10395)

user = User.query.get(int(25))
shipper = Shipper.query.get(int(3))
o10396 = Order(id=10396, customer=user, orderdate=datetime(1996, 12, 27), shipper=shipper)
db.session.add(o10396)

user = User.query.get(int(60))
shipper = Shipper.query.get(int(1))
o10397 = Order(id=10397, customer=user, orderdate=datetime(1996, 12, 27), shipper=shipper)
db.session.add(o10397)

user = User.query.get(int(71))
shipper = Shipper.query.get(int(3))
o10398 = Order(id=10398, customer=user, orderdate=datetime(1996, 12, 30), shipper=shipper)
db.session.add(o10398)

user = User.query.get(int(83))
shipper = Shipper.query.get(int(3))
o10399 = Order(id=10399, customer=user, orderdate=datetime(1996, 12, 31), shipper=shipper)
db.session.add(o10399)

user = User.query.get(int(19))
shipper = Shipper.query.get(int(3))
o10400 = Order(id=10400, customer=user, orderdate=datetime(1997, 1, 1), shipper=shipper)
db.session.add(o10400)

user = User.query.get(int(65))
shipper = Shipper.query.get(int(1))
o10401 = Order(id=10401, customer=user, orderdate=datetime(1997, 1, 1), shipper=shipper)
db.session.add(o10401)

user = User.query.get(int(20))
shipper = Shipper.query.get(int(2))
o10402 = Order(id=10402, customer=user, orderdate=datetime(1997, 1, 2), shipper=shipper)
db.session.add(o10402)

user = User.query.get(int(20))
shipper = Shipper.query.get(int(3))
o10403 = Order(id=10403, customer=user, orderdate=datetime(1997, 1, 3), shipper=shipper)
db.session.add(o10403)

user = User.query.get(int(49))
shipper = Shipper.query.get(int(1))
o10404 = Order(id=10404, customer=user, orderdate=datetime(1997, 1, 3), shipper=shipper)
db.session.add(o10404)

user = User.query.get(int(47))
shipper = Shipper.query.get(int(1))
o10405 = Order(id=10405, customer=user, orderdate=datetime(1997, 1, 6), shipper=shipper)
db.session.add(o10405)

user = User.query.get(int(62))
shipper = Shipper.query.get(int(1))
o10406 = Order(id=10406, customer=user, orderdate=datetime(1997, 1, 7), shipper=shipper)
db.session.add(o10406)

user = User.query.get(int(56))
shipper = Shipper.query.get(int(2))
o10407 = Order(id=10407, customer=user, orderdate=datetime(1997, 1, 7), shipper=shipper)
db.session.add(o10407)

user = User.query.get(int(23))
shipper = Shipper.query.get(int(1))
o10408 = Order(id=10408, customer=user, orderdate=datetime(1997, 1, 8), shipper=shipper)
db.session.add(o10408)

user = User.query.get(int(54))
shipper = Shipper.query.get(int(1))
o10409 = Order(id=10409, customer=user, orderdate=datetime(1997, 1, 9), shipper=shipper)
db.session.add(o10409)

user = User.query.get(int(10))
shipper = Shipper.query.get(int(3))
o10410 = Order(id=10410, customer=user, orderdate=datetime(1997, 1, 10), shipper=shipper)
db.session.add(o10410)

user = User.query.get(int(10))
shipper = Shipper.query.get(int(3))
o10411 = Order(id=10411, customer=user, orderdate=datetime(1997, 1, 10), shipper=shipper)
db.session.add(o10411)

user = User.query.get(int(87))
shipper = Shipper.query.get(int(2))
o10412 = Order(id=10412, customer=user, orderdate=datetime(1997, 1, 13), shipper=shipper)
db.session.add(o10412)

user = User.query.get(int(41))
shipper = Shipper.query.get(int(2))
o10413 = Order(id=10413, customer=user, orderdate=datetime(1997, 1, 14), shipper=shipper)
db.session.add(o10413)

user = User.query.get(int(21))
shipper = Shipper.query.get(int(3))
o10414 = Order(id=10414, customer=user, orderdate=datetime(1997, 1, 14), shipper=shipper)
db.session.add(o10414)

user = User.query.get(int(36))
shipper = Shipper.query.get(int(1))
o10415 = Order(id=10415, customer=user, orderdate=datetime(1997, 1, 15), shipper=shipper)
db.session.add(o10415)

user = User.query.get(int(87))
shipper = Shipper.query.get(int(3))
o10416 = Order(id=10416, customer=user, orderdate=datetime(1997, 1, 16), shipper=shipper)
db.session.add(o10416)

user = User.query.get(int(73))
shipper = Shipper.query.get(int(3))
o10417 = Order(id=10417, customer=user, orderdate=datetime(1997, 1, 16), shipper=shipper)
db.session.add(o10417)

user = User.query.get(int(63))
shipper = Shipper.query.get(int(1))
o10418 = Order(id=10418, customer=user, orderdate=datetime(1997, 1, 17), shipper=shipper)
db.session.add(o10418)

user = User.query.get(int(68))
shipper = Shipper.query.get(int(2))
o10419 = Order(id=10419, customer=user, orderdate=datetime(1997, 1, 20), shipper=shipper)
db.session.add(o10419)

user = User.query.get(int(88))
shipper = Shipper.query.get(int(1))
o10420 = Order(id=10420, customer=user, orderdate=datetime(1997, 1, 21), shipper=shipper)
db.session.add(o10420)

user = User.query.get(int(61))
shipper = Shipper.query.get(int(1))
o10421 = Order(id=10421, customer=user, orderdate=datetime(1997, 1, 21), shipper=shipper)
db.session.add(o10421)

user = User.query.get(int(27))
shipper = Shipper.query.get(int(1))
o10422 = Order(id=10422, customer=user, orderdate=datetime(1997, 1, 22), shipper=shipper)
db.session.add(o10422)

user = User.query.get(int(31))
shipper = Shipper.query.get(int(3))
o10423 = Order(id=10423, customer=user, orderdate=datetime(1997, 1, 23), shipper=shipper)
db.session.add(o10423)

user = User.query.get(int(51))
shipper = Shipper.query.get(int(2))
o10424 = Order(id=10424, customer=user, orderdate=datetime(1997, 1, 23), shipper=shipper)
db.session.add(o10424)

user = User.query.get(int(41))
shipper = Shipper.query.get(int(2))
o10425 = Order(id=10425, customer=user, orderdate=datetime(1997, 1, 24), shipper=shipper)
db.session.add(o10425)

user = User.query.get(int(29))
shipper = Shipper.query.get(int(1))
o10426 = Order(id=10426, customer=user, orderdate=datetime(1997, 1, 27), shipper=shipper)
db.session.add(o10426)

user = User.query.get(int(59))
shipper = Shipper.query.get(int(2))
o10427 = Order(id=10427, customer=user, orderdate=datetime(1997, 1, 27), shipper=shipper)
db.session.add(o10427)

user = User.query.get(int(66))
shipper = Shipper.query.get(int(1))
o10428 = Order(id=10428, customer=user, orderdate=datetime(1997, 1, 28), shipper=shipper)
db.session.add(o10428)

user = User.query.get(int(37))
shipper = Shipper.query.get(int(2))
o10429 = Order(id=10429, customer=user, orderdate=datetime(1997, 1, 29), shipper=shipper)
db.session.add(o10429)

user = User.query.get(int(20))
shipper = Shipper.query.get(int(1))
o10430 = Order(id=10430, customer=user, orderdate=datetime(1997, 1, 30), shipper=shipper)
db.session.add(o10430)

user = User.query.get(int(10))
shipper = Shipper.query.get(int(2))
o10431 = Order(id=10431, customer=user, orderdate=datetime(1997, 1, 30), shipper=shipper)
db.session.add(o10431)

user = User.query.get(int(75))
shipper = Shipper.query.get(int(2))
o10432 = Order(id=10432, customer=user, orderdate=datetime(1997, 1, 31), shipper=shipper)
db.session.add(o10432)

user = User.query.get(int(60))
shipper = Shipper.query.get(int(3))
o10433 = Order(id=10433, customer=user, orderdate=datetime(1997, 2, 3), shipper=shipper)
db.session.add(o10433)

user = User.query.get(int(24))
shipper = Shipper.query.get(int(2))
o10434 = Order(id=10434, customer=user, orderdate=datetime(1997, 2, 3), shipper=shipper)
db.session.add(o10434)

user = User.query.get(int(16))
shipper = Shipper.query.get(int(2))
o10435 = Order(id=10435, customer=user, orderdate=datetime(1997, 2, 4), shipper=shipper)
db.session.add(o10435)

user = User.query.get(int(7))
shipper = Shipper.query.get(int(2))
o10436 = Order(id=10436, customer=user, orderdate=datetime(1997, 2, 5), shipper=shipper)
db.session.add(o10436)

user = User.query.get(int(87))
shipper = Shipper.query.get(int(1))
o10437 = Order(id=10437, customer=user, orderdate=datetime(1997, 2, 5), shipper=shipper)
db.session.add(o10437)

user = User.query.get(int(79))
shipper = Shipper.query.get(int(2))
o10438 = Order(id=10438, customer=user, orderdate=datetime(1997, 2, 6), shipper=shipper)
db.session.add(o10438)

user = User.query.get(int(51))
shipper = Shipper.query.get(int(3))
o10439 = Order(id=10439, customer=user, orderdate=datetime(1997, 2, 7), shipper=shipper)
db.session.add(o10439)

user = User.query.get(int(71))
shipper = Shipper.query.get(int(2))
o10440 = Order(id=10440, customer=user, orderdate=datetime(1997, 2, 10), shipper=shipper)
db.session.add(o10440)

user = User.query.get(int(55))
shipper = Shipper.query.get(int(2))
o10441 = Order(id=10441, customer=user, orderdate=datetime(1997, 2, 10), shipper=shipper)
db.session.add(o10441)

user = User.query.get(int(20))
shipper = Shipper.query.get(int(2))
o10442 = Order(id=10442, customer=user, orderdate=datetime(1997, 2, 11), shipper=shipper)
db.session.add(o10442)

user = User.query.get(int(66))
shipper = Shipper.query.get(int(1))
o10443 = Order(id=10443, customer=user, orderdate=datetime(1997, 2, 12), shipper=shipper)
db.session.add(o10443)

db.session.commit()

print('Dummy Orders successfully added to database!')