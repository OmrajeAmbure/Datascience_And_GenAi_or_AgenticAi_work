from typing import Annotated

# pyright: reportMissingImports=false
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
import pandas as pd
import joblib
import numpy as np

app = FastAPI()

# Templates folder
templates = Jinja2Templates(directory="templates")
INDEX_TEMPLATE = "index.html"

# Load trained model
model = joblib.load(r"E:\AIandMl project\NIT Course\Python\ML\Student_Model\Desktop.pkl")

# DataFrame to store predictions
history_df = pd.DataFrame(columns=["study_hours", "Predicted_Output"])


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request,
        INDEX_TEMPLATE,
        {
            "request": request
        }
    )


@app.post("/predict")
async def predict(request: Request, study_hours: Annotated[float, Form(...)]):
    global history_df

    # Validate input
    if study_hours < 0 or study_hours > 24:
        return templates.TemplateResponse(
            request,
            INDEX_TEMPLATE,
            {
                "request": request,
                "prediction_text": "Please enter study hours between 0 and 24."
            }
        )

    # Create input with the same feature name used during training
    features = pd.DataFrame({
        "study_hours": [study_hours]
    })

    # Predict
    prediction = model.predict(features)

    # Convert prediction to a single float
    prediction = float(np.asarray(prediction).reshape(-1)[0])

    # Round to 2 decimal places
    prediction = round(prediction, 2)

    # Save prediction
    new_row = pd.DataFrame({
        "study_hours": [study_hours],
        "Predicted_Output": [prediction]
    })

    history_df = pd.concat([history_df, new_row], ignore_index=True)

    # Save CSV
    history_df.to_csv("smp_data_from_app.csv", index=False)

    return templates.TemplateResponse(
        request,
        INDEX_TEMPLATE,
        {
            "request": request,
            "prediction_text": f"Estimated Marks: {prediction}%"
        }
    )