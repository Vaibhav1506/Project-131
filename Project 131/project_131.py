# -*- coding: utf-8 -*-
"""Project 131.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XmKo4nAMyyYkK3ADNYWuBMNWXSJb1z_M
"""

from google.colab import files
filesToUpload = files.upload()

import csv
import pandas as pd
import plotly.express as px

row = []

df = pd.read_csv('final.csv')
df.head()

with open("final.csv", "r") as f:
  csvReader = csv.reader(f)

  for i in csvReader:
    row.append(i)


headers = row[0]
planet_data = row[1:] 

print(headers)
print(planet_data[0])

headers[0] = "row_num"

no_of_planet_in_solar_system = {}

for j in planet_data:
  if no_of_planet_in_solar_system.get(j[11]):
    no_of_planet_in_solar_system[j[11]]+=1
  else:
    no_of_planet_in_solar_system[j[11]] = 1
  
max_solar_system = max(no_of_planet_in_solar_system, key = no_of_planet_in_solar_system.get)

print("The Solar System {} has maximum planets {} out of the entire data".format(max_solar_system, no_of_planet_in_solar_system[max_solar_system]))

KOI_351_planet_list = []

for k in planet_data:
  if max_solar_system == k[11]:
    KOI_351_planet_list.append(k)
  
print(len(KOI_351_planet_list))
print(KOI_351_planet_list)

planet_data_conversion = list(planet_data)

for l in planet_data_conversion:
  planet_mass = l[3]
  
  if planet_mass == "Unknown":
    planet_data.remove(l)
    continue
  else:
    planet_mass_value = planet_mass.split(" ")[0]
    planet_mass_ref = planet_mass.split(" ")[1]
    
    if planet_mass_ref == "Jupiters":
      planet_mass_value = float(planet_mass_value) * 317.8 
    
    l[3] = planet_mass_value
    
    planet_radius = l[7]
    
    if planet_radius == "Unknown":
      planet_data.remove(l)
      continue
    else:
      planet_radius_value = planet_radius.split(" ")[0]
      planet_radius_ref = planet_radius.split(" ")[2]

      if planet_radius_ref == "Jupiters":
        planet_radius_value = float(planet_radius_value) * 11.2

    l[7] = planet_radius_value

print(len(planet_data))
print(planet_data_conversion)

KOI_351_planet_mass = []
KOI_351_planet_names = []

for m in KOI_351_planet_list:
  KOI_351_planet_mass.append(m[3])
  KOI_351_planet_names.append(m[1])

KOI_351_planet_mass.append(1)
KOI_351_planet_names.append("Earth")

fig = px.bar(x = KOI_351_planet_names, y = KOI_351_planet_mass)
fig.show()

planet_masses = []
planet_names = []
planet_radii = []

for n in planet_data:
  planet_masses.append(n[3])
  planet_radii.append(n[7])
  planet_names.append(n[1])

planet_gravity = []

for o, name in enumerate(planet_names):
  gravity = (float(planet_masses[o]) * 5.972e+24) / (float(planet_radii[o]) * float(planet_radii[o]) * 6371000 * 6371000) * 6.674e-11
  planet_gravity.append(gravity)

fig = px.scatter(x = planet_radii, y = planet_masses, size = planet_gravity, hover_data = [planet_names]) 
fig.show()

radius = df['planet_radius'].to_list()
mass = df['planet_mass'].to_list()
gravity =[]

def convert_to_si(radius,mass):
    for i in range(0,len(radius)-1):
        radius[i] = float(radius[i] * 6.957e+8)
        mass[i] = float(mass[i] * 1.989e+30)
        
convert_to_si(radius,mass)

def gravity_calculation(radius,mass):
    G = 6.674e-11
    for index in range(0,len(mass)):
        g= (mass[index]*G)/((radius[index])**2)
        gravity.append(g)
        
gravity_calculation(radius,mass)

df["Gravity"] = gravity
df