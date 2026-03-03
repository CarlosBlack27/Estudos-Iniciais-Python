distance_mi = 6
is_raining = True
has_bike = True
has_car = False
has_ride_share_app = False

if distance_mi <= 1 and is_raining == False:
  print("True")
elif distance_mi <= 1 and is_raining == True:
  print("False")
elif 1 < distance_mi  <= 6:
  if has_bike and not is_raining:
    print("True")
  else:
    print("False")
else:
  if distance_mi > 6  and has_car == True or has_ride_share_app == True:
    print("True")
  else:
    print("False")
