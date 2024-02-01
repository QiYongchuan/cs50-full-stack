from django.test import TestCase,Client
from django.db.models import Max

from .models import Airport,Flight,Passenger

# Create your tests here.
class FlightTestCase(TestCase):
  def setUp(self):
    #Create airports
    a1 = Airport.objects.create(code="AAA",city="City A")
    a2 = Airport.objects.create(code= "BBB",city="City B")
    
    #Create flights
    Flight.objects.create(origin=a1,destination=a2,duration=100)
    Flight.objects.create(origin=a1,destination=a1,duration=200)
    Flight.objects.create(origin=a1,destination=a2,duration=-100)
    
  def test_departures_count(self):
    a = Airport.objects.get(code="AAA")
    self.assertEqual(a.departures.count(),3)
    
  def test_arrivals_count(self):
    a = Airport.objects.get(code="AAA")
    self.assertEqual(a.arrivals.count(),1)

  def test_valid_flight(self):
    a1 = Airport.objects.get(code="AAA")
    a2 = Airport.objects.get(code = "BBB")
    f = Flight.objects.get(origin=a1,destination=a2,duration=100)
    self.assertTrue(f.is_valid_flight())
    #这里的is_valid_flight()是之前在代码model中写好的函数，来判断航班是否有效的；在这里进行测试， self.assertTrue（），
    # 是假定f = Flight.objects.get(origin=a1,destination=a2,duration=100)  这条数据是有效的航班，看代码是否也运行的结果是True
    
  def test_invalid_flight_destination(self):
    a1 = Airport.objects.get(code="AAA")
    f=Flight.objects.get(origin=a1,destination=a1)
    self.assertFalse(f.is_valid_flight())
    
  def test_invalid_flight_duration(self):
    a1 = Airport.objects.get(code="AAA")
    a2 = Airport.objects.get(code="BBB")
    f = Flight.objects.get(origin=a1,destination=a2,duration=-100)
    self.assertFalse(f.is_valid_flight())
    
  def test_index(self):
    c = Client()
    response = c.get("/flights/")
    self.assertEqual(response.status_code,200)
    self.assertEqual(response.context['flights'].count(),3)
    
  
  def test_valid_flight_page(self):
    a1 = Airport.objects.get(code="AAA")
    f = Flight.objects.get(origin = a1,destination=a1)
    
    c = Client()
    response  = c.get(f"/flights/{f.id}")
    self.assertEqual(response.status_code,200)
    
  # def test_invalid_flight_page(self):
  #   max_id =Flight.objects.all().aggregate(Max("id"))["id_max"]
    
  #   c = Client()
  #   response = c.get(f"/flights/{max_id +1}")
  #   self.assertEqual(response.status_code,404)