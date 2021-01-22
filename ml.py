from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

def test(features):
    url = "D:\opencv\index.csv"
    names = ['path', 'red', 'green', 'blue', 'diameter', 'jenis']
    dataset = read_csv(url, names=names)
    
    array = dataset.values
    X = array[:, 1:5]
    y = array[:, 5]
    X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20, random_state=1)
    
    model = LinearDiscriminantAnalysis()
    model.fit(X_train, Y_train)
    predictions = model.predict([features])
    
    predictions = predictions[0]
    return predictions
    