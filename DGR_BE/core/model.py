import tensorflow as tf

# Load the pre-trained MNIST model


def load_model():
    model = tf.keras.models.load_model('models/mnist_model.h5')
    return model
