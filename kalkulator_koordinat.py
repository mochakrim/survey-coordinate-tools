import math
import csv
import os

file_csv = "Data_Survey.csv"
def hitung():
    print("\n--- INPUT DATA ---")
    pt  =input("Nama Titik : ")
    x1  =float(input("X Alat   : "))
    y1  =float(input("y Alat   : "))
    z1  =float(input("z Alat   : "))

    print(f"Titik {pt} terdeteksi!")

    sd  =float(input("Jarak (SD) : "))
    az  =float(input("Azimuth    : "))
    zen =float(input("Zenith     : "))

    ar  =math.radians(az)
    zr  =math.radians(zen)

    hd  =sd * math.sin(zr)
    vd  =sd * math.cos(zr)

    x2 = x1 + (hd * math.sin(ar))
    y2 = y1 + (hd * math.cos(ar))
    z2 = z1 + vd

    print(f"\n--- HASIL HITUNG ---")
    print(f"X Baru: {x2:.3f}")
    print(f"Y Baru: {y2:.3f}")
    print(f"z Baru: {z2:.3f}")
hitung()

