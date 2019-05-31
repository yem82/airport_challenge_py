class Airport(object):

  def __init__(self, planes=[]):
    self.planes = planes

  def land_plane(self, plane):
   self.planes.append(plane)
