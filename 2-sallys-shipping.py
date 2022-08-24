w = 6.75 

# ground shipping
if w >= 2:
  cost_ground = w * 1.50 + 20
elif w >= 6:
  cost_ground = w * 3 + 20
elif w >= 10:
  cost_ground = w * 4 + 20
elif w > 10:
  cost_ground = w * 4.75 + 20
else:
  cost_ground = "error"
print("ground shipping: " + str(cost_ground))

# ground shipping premium
cost_ground_premium = 125
print("ground shipping premium: " + str(cost_ground_premium))

# drone shipping
if w >= 2:
  cost_drone = w * 4.50
elif w >= 6:
  cost_drone = w * 9
elif w >= 10:
  cost_drone = w * 12
elif w > 10:
  cost_drone = w * 14.25
else:
  cost_drone = "error"
print("drone shipping: " + str(cost_drone))
