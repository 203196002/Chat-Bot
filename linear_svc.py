import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.metrics import confusion_matrix
from matplotlib import style
style.use("ggplot") 
%matplotlib qt

x = [1,5,1.5,8,1,9]
y = [2,8,1.8,8,0.6,11]


plt.scatter(x,y)
plt.show()

X = np.array([
[1,2],
[5,8],
[1.5,1.8],
[8,8],
[1,0.6],
[9,11]])

Y = ['buy','sell','buy','sell','sell','buy']
clf = svm.SVC(kernel='linear', C=1.0)
clf.fit(X,Y)

print("Predction :", clf.predict([[10.58,10.76]]))

ypred = clf.predict(X)

cm = confusion_matrix(Y,ypred)
print(cm)
# look at the documentation of confusion_matrix at https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html

# Visualization
#initialize weights
w = clf.coef_[0]
print(w)

a = -w[0]/w[1]

xx = np.linspace(0,12)
yy = a * xx -clf.intercept_[0] / w[1]

h0 = plt.plot(xx,yy, 'k-', label='non weighted division')
plt.scatter(X[:,0], X[:,1],c='#17becf')
plt.show() 