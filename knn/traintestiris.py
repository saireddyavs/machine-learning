import pandas as pd
import numpy as np
import math
import operator

import warnings
warnings.filterwarnings("ignore")
col=['sepal_length','sepal_width','petal_length','petal_width','type']
iris=pd.read_csv("iris.xlsx",names=col)
from sklearn.model_selection import train_test_split

#iris1=pd.read_csv("iris.xlsx")

x=iris.iloc[1:,:3]
y=iris.iloc[1:,4:]
#print(y.head())
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

cv_scores = []
neighbors = list(np.arange(3,50,4))
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

from sklearn.metrics import accuracy_score
for n in neighbors:
    knn = KNeighborsClassifier(n_neighbors = n,algorithm = 'brute')
    #knn = KNeighborsClassifier(n_neighbors = n,algorithm = 'kd_tree',leaf_size = 30)
    cross_val = cross_val_score(knn,x_train,y_train,cv = 5 , scoring = 'accuracy')
    cv_scores.append(cross_val.mean())
    
error = [1-x for x in cv_scores]
optimal_n = neighbors[ error.index(min(error)) ]
knn_optimal = KNeighborsClassifier(n_neighbors = optimal_n,algorithm = 'brute')
knn_optimal.fit(x_train,y_train)
pred = knn_optimal.predict(x_test)
acc = accuracy_score(y_test,pred)*100

print("The accuracy for optimal k = {0} using brute is {1}".format(optimal_n,acc))

from sklearn.metrics import classification_report
print("classification_report")
print(classification_report(y_test,pred))

from sklearn.metrics import recall_score , precision_score , roc_auc_score ,roc_curve
from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import unique_labels
cm = confusion_matrix(y_test, pred)
print(cm)
cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
classes=col[:,np.newaxis]
classes = classes[unique_labels(y_test, pred)]
fig, ax = plt.subplots()
im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
ax.figure.colorbar(im, ax=ax)
    # We want to show all ticks...
ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           # ... and label them with the respective list entries
           xticklabels=classes, yticklabels=classes,
           title=title,
           ylabel='True label',
           xlabel='Predicted label')

    # Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
fmt = '.2f' if normalize else 'd'
thresh = cm.max() / 2.
for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        ax.text(j, i, format(cm[i, j], fmt),
            ha="center", va="center",
            color="white" if cm[i, j] > thresh else "black")
fig.tight_layout()
plt.show()



