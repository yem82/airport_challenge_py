import unittest
from airport import Airport
from plane import Plane

class TestAirport(unittest.TestCase):

  def setUp(self):

    self.airport = Airport()
    self.plane = Plane()

  def test_empty_at_initialization(self):
    """airport has no planes"""
    self.assertEqual(self.airport.planes, [])

  def test_land_plane(self):
    """a plane can land at an airport"""
    self.airport.land_plane(self.plane)
    self.assertEqual(self.airport.planes, [self.plane])


if __name__ == '__main__':
    unittest.main()
