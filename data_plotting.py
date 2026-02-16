import pandas as pd
import matplotlib.pyplot as plt

file_path = 'data.csv'   
data = pd.read_csv(file_path)

durata = data['Durata']
puls = data['Puls']
maxpuls = data['MaxPuls']
calorii = data['Calorii']

X =len("Mihai")
Y = len("AndreiDaniel")

plt.figure()
plt.plot(durata, label='Durata',color="blue")
plt.plot(puls, label='Puls',color="green")
plt.plot(maxpuls, label='Max Puls',color="fuchsia")
plt.plot(calorii, label="Calorii",color="purple")
plt.title("toate valorile")
plt.show()

plt.figure()
plt.plot(durata[:X], label='Durata (primele X valori)',color="indigo")
plt.plot(puls[:X], label='Puls (primele X valori)',color="magenta")
plt.plot(maxpuls[:X], label='Max Puls',color="orange")
plt.plot(calorii[:X], label="Calorii",color="blue")
plt.title(f"primele {X} valori")
plt.show()

plt.figure()
plt.plot(durata[-Y:], label='Durata (ultimele Y valori)',color="green")
plt.plot(puls[-Y:], label='Puls (ultimele Y valori)',color="yellow")
plt.title(f"ultimele {Y} valori")
plt.show()