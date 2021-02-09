from sklearn.neural_network import MLPRegressor
import numpy as np
#读入数据get train data in

trdatas = np.loadtxt("train_data.txt", encoding='utf-8', skiprows=1)
trtruths = np.loadtxt("train_truth.txt", encoding='utf-8', skiprows=1)

clf = MLPRegressor(hidden_layer_sizes=(4,4))
clf.fit(trdatas,trtruths)

#get in test data

testdatas = np.loadtxt("test_data.txt", encoding='utf-8', skiprows=1)

predict_truth = clf.predict(testdatas)

result= open("test_predict.txt","a")
result.write("y\n")
for i in predict_truth:
    result.write(str(i))
    result.write("\n")
result.close()
