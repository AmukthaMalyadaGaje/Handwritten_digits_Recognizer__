from fastapi import APIRouter, File, UploadFile, HTTPException
from PIL import Image
import numpy as np
from utils import preprocess_image
from tensorflow.keras.models import load_model
import io

router = APIRouter()

# Load the trained MNIST model
model = load_model('mnist_model.h5')


@router.post("/predict-digit")
async def predict_digit(file: UploadFile = File(...)):
    try:
        # Check the content type of the uploaded file
        if file.content_type not in ['image/jpeg', 'image/png', 'image/jpg']:
            raise HTTPException(
                status_code=400, detail="Invalid image type. Only JPEG and PNG are accepted."
            )

        # Open the image file
        image = Image.open(file.file)

        # Preprocess the image
        processed_image = preprocess_image(image)
        # This should print (1, 28, 28, 1)
        print("Shape:", processed_image.shape)

        # Perform the prediction
        prediction = model.predict(processed_image)
        predicted_digit = np.argmax(prediction)
        # Print softmax probabilities
        print("Prediction Probabilities:", prediction)
        print("Predicted Digit: ", predicted_digit)

        return {"predicted_digit": int(predicted_digit)}

    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Error processing image: {str(e)}"
        )
