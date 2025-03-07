# Libraries
import seaborn as sns
import matplotlib.pyplot as plt

# load dataset
data = sns.load_dataset('titanic')

# plot
sns.violinplot(data=data, x='class',y='age', hue='alive') 
plt.show()

