from core.model import load_model
from utils import preprocess_image

model = load_model()


def predict_digit(image):
    # Preprocess the image
    processed_image = preprocess_image(image)
    # Predict the digit
    prediction = model.predict(processed_image)
    predicted_digit = prediction.argmax()
    return predicted_digit
