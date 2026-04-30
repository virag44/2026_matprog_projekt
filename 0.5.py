import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def expected_height(m_height,f_height,boy=True):
  if boy==True:
    m=(m_height+f_height+13)/2
    return f'{m}cm a várható magasság, ez azt jelenti hogy a gyerek {m-10}-{m+10} centiméter közötti magas lesz'
  else:
    m=(m_height+f_height-13)/2
    return f'{m}cm a várható magasság, ez azt jelenti hogy a gyerek {m-10}-{m+10} centiméter közötti magas lesz'
expected_height(155,185,False)

x_labels = []
y_labels = []
y = []

with open("férfi_magasságok.txt", "r") as file:
    for line in file:
        line = line.strip()

        if line.count(",") == 2:
            orszag, magasag, y_ertek = line.split(',')

            x_labels.append(orszag)
            y_labels.append(magasag)
            y.append(int(y_ertek))


x_labels2 = []
y_labels2 = []
y2 = []

with open("női_magasságok.txt", "r") as file:
    for line in file:
        line = line.strip()

        if line.count(",") == 2:
            orszag, magassag, y_ertek = line.split(',')

            x_labels2.append(orszag)
            y_labels2.append(magassag)
            y2.append(int(y_ertek))


x_labels3 = []
y3 = []

with open("orszagok_stress.txt", "r") as file:
  for line in file:
    line = line.strip()
    orszag, y_ertek = line.split(',')

    x_labels3.append(orszag)
    y3.append(int(y_ertek))
    

fig, axs = plt.subplots(2, 2, figsize=(9, 10))

x = np.arange(len(y))

axs[0,0].bar(x, y, color='#42f5cb')   
axs[0,0].set_xticks(x)      
axs[0,0].set_xticklabels(x_labels, rotation=45, ha='right')    
axs[0,0].set_yticks(y)          
axs[0,0].set_yticklabels(y_labels)   
axs[0,0].set_title("Férfiak átlagmagassága")   
axs[0,0].set_ylabel('Magasságok')
axs[0,0].set_xlabel('országok')



x2 = np.arange(len(y2))

axs[0,1].bar(x, y2, color='#8442f5')
axs[0,1].set_xticks(x)
axs[0,1].set_xticklabels(x_labels2, rotation=45, ha='right') 
axs[0,1].set_yticks(y2)
axs[0,1].set_yticklabels(y_labels2)
axs[0,1].set_title("Nők átlagmagassága")
axs[0,1].set_ylabel('Magasságok')
axs[0,1].set_xlabel('országok')

x3 = np.arange(len(y3))

axs[1,0].bar(x, y3, color='#f54284')
axs[1,0].set_xticks(x)
axs[1,0].set_xticklabels(x_labels3, rotation=45, ha='right') 
axs[1,0].set_yticks(y3)
axs[1,0].set_title('')
axs[1,0].set_xlabel('országok')

labels_k= ['nem', 'igen']
sizes = [70,30 ]

axs[1, 1].pie(sizes, labels=labels_k, autopct= '%1.0f%%') 
                                                      


plt.tight_layout()
plt.show()
