import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load the dataset
file_path = 'Titanic Dataset.csv'  # Update this with the correct path to your dataset
titanic_df = pd.read_csv(file_path)

# Selecting relevant features
features = titanic_df[['pclass', 'sex', 'age']]
target = titanic_df['survived']

# Handling missing values in 'age'
imputer = SimpleImputer(strategy='median')
features.loc[:, 'age'] = imputer.fit_transform(features[['age']])

# Encoding categorical variable 'sex'
label_encoder = LabelEncoder()
features.loc[:, 'sex'] = label_encoder.fit_transform(features['sex'])

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Training the logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluating the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"Model Accuracy: {accuracy}")
print(f"Classification Report:\n{report}")

# Prediction function
def predict_survival(age, sex, pclass):
    # Encode the input features
    sex_encoded = label_encoder.transform([sex])[0]
    
    # Prepare the feature array
    features = pd.DataFrame([[pclass, sex_encoded, age]], columns=['pclass', 'sex', 'age'])
    
    # Predict the survival
    prediction = model.predict(features)
    
    # Return the prediction
    return "Survived" if prediction[0] == 1 else "Did not survive"

# Example usage
# Example usage
example1 = (29, 'female', 1)
example2 = (40, 'male', 3)
print(f"Input: Age={example1[0]}, Sex={example1[1]}, Class={example1[2]} => Prediction: {predict_survival(*example1)}")
print(f"Input: Age={example2[0]}, Sex={example2[1]}, Class={example2[2]} => Prediction: {predict_survival(*example2)}")