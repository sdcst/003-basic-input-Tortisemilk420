#! python3
# Find the volume of a sphere.
# You will ask the user to enter the radius of the sphere.
# Calculate the Volume and then display the result to the user.
# You will need to import the math module in order to use math.pi

# Inputs:
# radius
#
# Outputs
# volume
#
# test output radius of 3 should give volume of 113.097335529232


import math

def calculate_sphere_volume(radius):
    volume = (4/3) * math.pi * (radius ** 3)
    return volume

def main():
  
    radius_str = input("Enter the radius of the sphere: ")

    radius = float(radius_str)

    volume = calculate_sphere_volume(radius)

    print(f"The volume of the sphere with radius {radius} is: {volume:.15f}")

if __name__ == "__main__":
    main()
