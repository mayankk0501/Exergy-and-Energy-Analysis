import pandas as pd
import matplotlib.pyplot as plt
import math

energy_efficiency_values = []
exergy_efficiency_values = []
intensity_values = []

df = pd.read_excel("data.xlsx")
for index,row in df.iterrows():
    flow_rate = row['Mass flow rate']
    Cp = row['Specific heat of fluid']
    Tin = row['Inlet Temperature']
    Tout = row['Outlet Temperature']
    Asc = row['Area of Solar collector']
    I = row['Solar Intensity']
    Tatm = row['Atmospheric Temperature']
    Ts = row['Source Temperature']

    Energy_Efficiency = (flow_rate*Cp*(Tout-Tin))/(Asc*I)
    Exergy_Efficiency = (flow_rate*Cp*((Tout-Tin)-(Tatm*(math.log(Tout/Tin)))))/(Asc*I*(1-(Tatm/Ts)))

    energy_efficiency_values.append(Energy_Efficiency)
    exergy_efficiency_values.append(Exergy_Efficiency)
    intensity_values.append(I)

plt.plot(intensity_values, energy_efficiency_values, marker='o', label='Energy Efficiency')
plt.xlabel('Solar Intensity')
plt.ylabel('Energy Efficiency')
plt.title('Energy Efficiency vs Solar Intensity')
plt.grid(True)
plt.show()

plt.plot(intensity_values, exergy_efficiency_values, marker='o', label='Exergy Efficiency')
plt.xlabel('Solar Intensity')
plt.ylabel('Exergy Efficiency')
plt.title('Exergy Efficiency vs Solar Intensity')
plt.grid(True)
plt.show()