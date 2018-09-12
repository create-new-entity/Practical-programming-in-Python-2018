def print_distance(p1, p2, prec=2):
  d = (((p1[0]-p2[0])*(p1[0]-p2[0])) + ((p1[1]-p2[1])*(p1[1]-p2[1]))) ** 0.5
  print("Distance between {} and {} with {} decimals is {:.{}f}".format(p1, p2, prec, d, prec))