import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np

# df = sns.load_dataset('tips')
# print(df.head())

# melihat dataset bawaan seaborn
# print(sns.get_dataset_names())

def plotsin(flip = 1):
    x = np.linspace(0, 14, 100)
    for i in range(1, 5):
        plt.plot(x, np.sin(x + i * 0.5) * (7 -1) * flip)
sns.set()
plotsin()
plt.show()