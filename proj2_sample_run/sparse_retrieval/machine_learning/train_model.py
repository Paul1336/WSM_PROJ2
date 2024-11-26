import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

class RandomForestModel:
    def __init__(self, X_train, y_train):
        self.rf = RandomForestClassifier(max_features='sqrt', bootstrap=False)
        self.rf.fit(X_train, y_train)

    def predict(self, X_test):
        return self.rf.predict(X_test)

class LogisticRegressionModel:
    def __init__(self, X_train, y_train):
        self.lr = LogisticRegression(class_weight='balanced', max_iter=1000)
        self.lr.fit(X_train, y_train)

    def predict(self, X_test):
        return self.lr.predict_proba(X_test)[:, 1]


def main():
    train_file = './train.xlsx'
    train_data = pd.read_excel(train_file)
    print(f"data read, including {train_data.shape[0]} rows, {train_data.shape[1]} cols")

    test_file = './test.xlsx'
    test_data = pd.read_excel(test_file)
    print(f"data read, including {test_data.shape[0]} rows, {test_data.shape[1]} cols")

    X_train = train_data[['Score 1', 'Score 2', 'Score 3']].values
    y_train = train_data['Last Value'].values
    X_test = test_data[['Score 1', 'Score 2', 'Score 3']].values

    #model = RandomForestModel(X_train, y_train)
    model = LogisticRegressionModel(X_train, y_train)

    predictions = model.predict(X_test)
    print(predictions)

    test_data['Predictions'] = predictions
    output_file = './predictions_full_weighted.xlsx'
    test_data.to_excel(output_file, index=False)


if __name__ == "__main__":
    main()