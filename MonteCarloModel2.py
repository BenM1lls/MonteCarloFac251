import random

def calculate_stress(weight, distance):
  """
  Calculates the stress on a square meter from a single person.

  Args:
      weight: Weight of the person in kg.
      distance: Distance in meters between the person and the point of interest.

  Returns:
      Stress on the square meter in kN. (Assuming gravity = 9.81 m/s^2)
  """
  gravity = 9.81  # m/s^2
  area_of_foot = 0.1  # m^2 (average)
  stress = weight * gravity / (4 * distance**2 * area_of_foot)  
  return stress / 1000  # convert N to kN

def simulate_room(room_width, room_length, max_stress):
  """
  Runs a Monte Carlo simulation to find the maximum number of people before exceeding stress limit.

  Args:
      room_width: Width of the room in meters.
      room_length: Length of the room in meters.
      max_stress: Maximum stress allowed on a square meter in kN.

  Returns:
      Number of people added before exceeding the stress limit or -1 if no limit is reached within 1000 iterations.
  """
  total_stress = 0
  people = []
  for _ in range(1000):
    weight = random.uniform(65, 85)  # Random weight between 65 and 85 kg
    x = random.uniform(0, room_width)  # Random X position
    y = random.uniform(0, room_length)  # Random Y position
    people.append((weight, x, y))
    for px, py in people:
      distance = min(abs(x - px), room_width - abs(x - px), abs(y - py), room_length - abs(y - py))
      total_stress += calculate_stress(weight, distance)
      if total_stress > max_stress:
        return len(people)
  return -1

# Define room dimensions and maximum stress
room_width = 6
room_length = 12
max_stress = 5

# Run the simulation
num_people = simulate_room(room_width, room_length, max_stress)

if num_people == -1:
  print("No limit reached within 1000 iterations.")
else:
  print(f"Maximum number of people before exceeding {max_stress} kN/m^2 stress: {num_people}")