from flask import Flask, request, jsonify
import tensorflow as tf
from PIL import Image
import numpy as np
import io
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024  # 5 MB upload limit

# Load model
model = tf.keras.models.load_model("my_models/Cotton_plant_disease_v1_98_22.keras")

# Define class labels (ensure this matches your model's output shape)
class_names = [
    "Aphids",
    "Army worm",
    "Bacterial blight",
    "Cotton Boll Rot",
    "Green Cotton Boll",
    "Healthy",
    "Powdery mildew",
    "Target spot"
]

# Preprocessing function
def preprocess_image(image_bytes):
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    img = img.resize((224, 224))  # Use your model’s expected input size
    img_array = np.array(img) / 255.0
    return np.expand_dims(img_array, axis=0)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/predict", methods=["POST"])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    if not file or not file.filename:
        return jsonify({"error": "Empty file upload"}), 400
    img_bytes = file.read()
    if not img_bytes:
        return jsonify({"error": "Uploaded file has no content"}), 400

    try:
        # Preprocess and predict
        input_tensor = preprocess_image(img_bytes)
        predictions = model.predict(input_tensor, verbose=0)

        # Check shape matches
        if predictions.shape[1] != len(class_names):
            return jsonify({
                "error": "Mismatch between prediction output and class_names length",
                "prediction_shape": predictions.shape,
                "num_classes": len(class_names)
            }), 500

        predicted_class_index = int(np.argmax(predictions))
        predicted_class = class_names[predicted_class_index]

        return jsonify({
            "predicted_class": predicted_class,
            "confidence": float(np.max(predictions))
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
