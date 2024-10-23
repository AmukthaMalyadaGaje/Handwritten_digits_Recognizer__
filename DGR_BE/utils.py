import numpy as np
from PIL import Image
from PIL import ImageOps


def preprocess_image(image: Image.Image):
    # Convert to grayscale if not already
    if image.mode != "L":
        image = ImageOps.grayscale(image)

    # Resize the image to 28x28 pixels
    image = image.resize((28, 28))

    # Convert the image to a numpy array and normalize pixel values
    image_array = np.array(image).astype('float32') / 255.0

    # Reshape the array to (1, 28, 28, 1)
    image_array = np.expand_dims(image_array, axis=(0, -1))

    return image_array
