def calculate_area():
    print("--- Land Area Calculator (Coordinate Method) ---")
     
    try:
        n = int(input("Enter the number of points/boundary markers: "))
        if n < 3:
            print("Error: A polygon must have at least 3 points.")
            return
 
        x = []
        y = []
 
        for i in range(n):
            print(f"\nPoint {i+1}:")
            xi = float(input(f"  Enter X{i+1}: "))
            yi = float(input(f"  Enter Y{i+1}: "))
            x.append(xi)
            y.append(yi)
 
        # Shoelace Formula for area calculation
        area = 0.0
        for i in range(n):
            j = (i + 1) % n
            area += x[i] * y[j]
            area -= x[j] * y[i]
         
        area = abs(area) / 2.0
 
        print("\n--- Calculation Results ---")
        print(f"Total Area: {area:.3f} sq meters (m2)")
        print(f"Total Area: {area/10000:.4f} Hectares")
         
    except ValueError:
        print("Invalid input. Please enter numbers only.")
 
if __name__ == "__main__":
    calculate_area()
