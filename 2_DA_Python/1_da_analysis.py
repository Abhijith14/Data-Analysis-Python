import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


data_source = 'http://wiki.stat.ucla.edu/socr/index.php/SOCR_Data_Dinov_020108_HeightsWeights'
data = pd.read_html(data_source)
df = data[1]

relation = df.corr()

plt.figure(figsize=(15, 10))
sns.heatmap(relation, annot=True, cmap='viridis_r')
plt.show()
