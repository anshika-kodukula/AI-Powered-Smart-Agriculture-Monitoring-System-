import random

def predict_disease():
    predictions = [
        ("Healthy", 96),
        ("Early Blight", 94),
        ("Leaf Spot", 91),
        ("Late Blight", 92)
    ]

    return random.choice(predictions)