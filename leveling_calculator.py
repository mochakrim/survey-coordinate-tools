import math
 
def leveling_survey():
    print("--- Digital Leveling Sheet (Sipat Datar) ---")
     
    # 1. Input Bench Mark Elevation
    elev_bm = float(input("Enter BM Elevation (m): "))
     
    # 2. Input Backsight reading
    bs = float(input("Enter Backsight (BS) reading (m): "))
     
    # Calculate Height of Instrument
    hi = elev_bm + bs
    print(f"\n>> Height of Instrument (HI): {hi:.3f} m")
     
    print("\n--- Point Readings ---")
    while True:
        point_name = input("\nPoint Name (or type 'done' to finish): ")
        if point_name.lower() == 'done':
            break
             
        # 3. Input Foresight reading
        fs = float(input(f"Enter Foresight (FS) reading at {point_name} (m): "))
         
        # Calculate Elevation
        new_elev = hi - fs
        diff = new_elev - elev_bm
         
        print(f"Result for {point_name}: Elev = {new_elev:.3f} m | Diff = {diff:.3f} m")
 
    print("\nCalculation Finished.")
 
if __name__ == "__main__":
    leveling_survey()
