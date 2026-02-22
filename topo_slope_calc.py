import math
 
def calculate_slope():
    """
    Calculates the slope angle and grade percentage 
    based on distance and elevation data.
    """
    print("--- Slope & Gradient Calculator (Surveying) ---")
    try:
        # User Inputs
        dist = float(input("Enter Horizontal Distance (m): "))
        elev1 = float(input("Enter Elevation of Point A (m): ")) 
        elev2 = float(input("Enter Elevation of Point B (m): "))
         
        # Calculate vertical difference
        delta_h = abs(elev2 - elev1)
         
        # Calculate slope angle in radians
        angle_rad = math.atan(delta_h / dist)
         
        # Convert radians to degrees (Fixed the 'angle' spelling!)
        angle_deg = math.degrees(angle_rad)
         
        # Calculate grade percentage
        grade = (delta_h / dist) * 100
         
        # Output results
        print("-" * 40)
        print(f"Results for your survey data:")
        print(f"Vertical Diff (ΔH) : {delta_h:.3f} m")
        print(f"Slope Angle        : {angle_deg:.2f}°")
        print(f"Grade Percentage   : {grade:.2f}%")
        print("-" * 40)
 
    except ValueError:
        print("Error: Invalid input. Please enter numerical values.")
    except ZeroDivisionError:
        print("Error: Distance cannot be zero.")
 
if __name__ == "__main__":
    calculate_slope()
