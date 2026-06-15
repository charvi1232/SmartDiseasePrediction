import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# =========================================
# LOAD DATASET
# =========================================

data = pd.read_csv("final_disease_data.csv")

# =========================================
# INPUT FEATURES
# =========================================

X = data.drop("disease", axis=1)

# =========================================
# OUTPUT LABEL
# =========================================

y = data["disease"]

# =========================================
# TRAIN MACHINE LEARNING MODEL
# =========================================

model = DecisionTreeClassifier()

model.fit(X, y)

# =========================================
# DISEASE PREDICTION FUNCTION
# =========================================

def predict_disease(symptoms):

    # If no symptoms selected

    if sum(symptoms) == 0:

        return "No Major Disease Detected"

    # Predict disease

    result = model.predict([symptoms])

    prediction = result[0]

    # Improve prediction logic

    fever = symptoms[0]
    cough = symptoms[1]
    headache = symptoms[2]
    fatigue = symptoms[3]
    nausea = symptoms[4]
    body_pain = symptoms[5]
    sore_throat = symptoms[6]
    vomiting = symptoms[7]
    dizziness = symptoms[8]
    cold = symptoms[9]

    # Viral Fever / Flu Conditions

    if fever and cough and cold:

        prediction = "Flu"

    elif fever and body_pain and fatigue:

        prediction = "Viral Fever"

    elif cold and cough and sore_throat:

        prediction = "Common Cold"

    elif headache and dizziness:

        prediction = "Migraine"

    elif nausea and vomiting:

        prediction = "Food Poisoning"

    return prediction