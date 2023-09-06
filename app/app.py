# app/app.py
# Model serving

from flask import Flask
import torch
from models.mnist_model import MNISTModel 

app = Flask(__name__)

# Load trained model
model = MNISTModel()
model.load_state_dict(torch.load('mnist_model.pth'))
model.eval()

# Prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
  # Get image from request
  image = request.files['image']
  
  # Predict digit and return result
  output = model(image)
  digit = torch.argmax(output)
  return {'digit': digit}
  
if __name__ == '__main__':
    app.run()