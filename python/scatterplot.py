import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import matplotlib
import seaborn as sns
from matplotlib.ticker import MaxNLocator
from scipy.stats import gaussian_kde


y_pred = pd.read_csv("dev_evaluation_16mars_rgb_resnet_linear-1.txt", skiprows=6, header=None, sep=" ")
y_pred = pd.read_csv("mse17_inceptV4_maxpool_cropped_no_zca_pairs.csv", skiprows=0, header=None, sep=" ")

scatter = pd.DataFrame()
scatter['Age'] = round(y_pred[2].astype(str).str[2:].astype(np.float)).astype(np.int)
scatter['y_pred'] = round(y_pred[1].astype(str).str[:-1].astype(np.float)).astype(np.int)

#singles prediction
scatter = pd.DataFrame()
scatter['y_pred'] = pd.Series.append(y_pred[1], y_pred[2])
scatter['Age'] =  pd.Series.append(y_pred[0], y_pred[0])

#for test-set - pairs
scatter = pd.DataFrame()
scatter['Age'] = y_pred[0]
scatter['y_pred'] = (y_pred[3])

scatter = pd.DataFrame()
scatter['Age'] =  pd.Series.append(df['age'], df['age'])
scatter['y_pred'] = pd.Series.append(df['left'], df['right'])

scatter = pd.DataFrame()
scatter['Age'] = df['age']
scatter['y_pred'] = df['mean']

matplotlib.rc('xtick', labelsize=12) 
matplotlib.rc('ytick', labelsize=12) 
matplotlib.pyplot.yticks(range(0, scatter['Age'].max()+1 ))
matplotlib.pyplot.xticks(range(0, scatter['Age'].max()+1 ))
range_values = range(1, scatter['Age'].max()+1)
plt.plot(range_values, range_values) 
plt.scatter(scatter['Age'], scatter['y_pred'])
#plt.scatter(scatter['Age'], scatter['y_pred'], c=z, s=100, edgecolor='', cmap='viridis')
plt.ylabel('Predicted age', fontsize=16)
plt.xlabel('Reader age', fontsize=16)
plt.savefig('fig4a_single.eps', format='eps', dpi=600)
plt.savefig('fig4a_single.tif', format='tif', dpi=600)
plt.show()

#scatter['y_pred'] = pd.Series.round(y_pred[3]).astype(np.int)



#Left right prediction
scatter = pd.DataFrame()


scatter['left'] = y_pred[1]
scatter['right'] = y_pred[2]
scatter['Age'] = y_pred[0]
matplotlib.rc('xtick', labelsize=16) 
matplotlib.rc('ytick', labelsize=16) 
matplotlib.pyplot.yticks(range(0, scatter['Age'].max()+1 ))
matplotlib.pyplot.xticks(range(0, scatter['Age'].max()+1 ))
range_values = range(1, scatter['Age'].max()+1)
plt.plot(range_values, range_values) 
plt.scatter(scatter['left'], scatter['right'])
plt.ylabel('Right otolith prediction', fontsize=18)
plt.xlabel('Left otolith prediction', fontsize=18)
plt.show()

#left vs expert
scatter = pd.DataFrame()
#scatter['y_pred'] = pd.Series.append(y_pred[1], y_pred[2])
#scatter['Age'] =  pd.Series.append(y_pred[0], y_pred[0])

scatter['left'] = df[3]
scatter['Age'] = y_pred[0]
matplotlib.rc('xtick', labelsize=16) 
matplotlib.rc('ytick', labelsize=16) 
matplotlib.pyplot.yticks(range(0, scatter['Age'].max()+1 ))
matplotlib.pyplot.xticks(range(0, scatter['Age'].max()+1 ))
range_values = range(1, scatter['Age'].max()+1)
plt.plot(range_values, range_values) 
plt.scatter(scatter['Age'], scatter['left'])
plt.ylabel('Predicted age', fontsize=18) #('Right otolith prediction', fontsize=18)
plt.xlabel('Read age', fontsize=18)
plt.show()


xy = np.vstack([scatter['Age'],scatter['y_pred']])
z = gaussian_kde(xy)(xy)

matplotlib.rc('xtick', labelsize=16) 
matplotlib.rc('ytick', labelsize=16) 
matplotlib.pyplot.yticks(range(0, scatter['Age'].max()+1 ))
matplotlib.pyplot.xticks(range(0, scatter['Age'].max()+1 ))
range_values = range(1, scatter['Age'].max()+1)
plt.plot(range_values, range_values) 
plt.scatter(scatter['Age'], scatter['y_pred'])
#plt.scatter(scatter['Age'], scatter['y_pred'], c=z, s=100, edgecolor='', cmap='viridis')
plt.ylabel('Predicted age', fontsize=18)
plt.xlabel('Read age', fontsize=18)
plt.show()

plt.colorbar()


#sns.lmplot(x='Age',y='y_pred',data=scatter,fit_reg=True)
#sns.regplot(x="Age", y="y_pred", data=scatter)

########## BOX PLOT ###############
scatter = pd.DataFrame()
scatter['Age'] = y_pred[0]
scatter['y_pred'] = y_pred[3]

matplotlib.pyplot.yticks(range(0, scatter['Age'].max()+1 ))
matplotlib.pyplot.xticks(range(0, scatter['Age'].max()+1 ))
range_values = range(0, scatter['Age'].max()+1)
plt.plot(range_values,range_values)
sns.boxplot(y='y_pred', x='Age', data=scatter)

plt.show()

###### LOSS PLOT ######################
scatter = pd.DataFrame()
scatter['training_loss'] = loss[0]
scatter['validation_loss'] = val_loss[0]
scatter.plot()
plt.ylabel('Loss')
plt.xlabel('Epochs')

###### plot MSE ###############
import pandas as pd
from matplotlib import pyplot
val_mse = pd.read_csv('val_mse_history_1mars_hillshade_resnet_linear-1.txt', header=None)
mse = pd.read_csv('mse_history_1mars_hillshade_resnet_linear-1.txt', header=None)

fig, ax = pyplot.subplots()
l1, = ax.plot(mse[0], color='green', label="training MSE")
l2, = ax.plot(val_mse[0], color='red', label="dev MSE")
legend = ax.legend(loc='upper center', shadow=True, fontsize='x-large')

pyplot.show()
