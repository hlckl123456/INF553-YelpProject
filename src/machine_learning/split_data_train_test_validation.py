from sklearn.model_selection import train_test_split
import pandas as pd

def splitData(filename):
    dataframe = pd.read_csv(filename)
    X = dataframe.drop(['current_grade','current_score','inspection_grade','inspection_score'],axis=1)
    y = dataframe[['inspection_grade']]
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=1, shuffle=False)
    X_train, X_validate,y_train, y_validate = train_test_split(X_train,y_train, test_size=0.25, random_state=1, shuffle=False)
    
    #X_train.to_csv("/Users/apple/Desktop/X_train.csv", encoding='utf-8', index=False)
    #y_train.to_csv("/Users/apple/Desktop/y_train.csv", encoding='utf-8', index=False)
    #X_test.to_csv("/Users/apple/Desktop/X_test.csv", encoding='utf-8', index=False)
    #y_test.to_csv("/Users/apple/Desktop/y_test.csv", encoding='utf-8', index=False)
    #X_validate.to_csv("/Users/apple/Desktop/X_validate.csv", encoding='utf-8', index=False)
    #y_validate.to_csv("/Users/apple/Desktop/y_validate.csv", encoding='utf-8', index=False)
    return X_train, y_train, X_test,y_test,X_validate,y_validate


if __name__ == "__main__":
    splitData("/Users/apple/Desktop/final_lasvegas_dataset.csv")
