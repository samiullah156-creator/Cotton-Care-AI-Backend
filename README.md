# Cotton Care AI Backend

Flask API that classifies cotton leaf images with a TensorFlow CNN. It powers the [Cotton-Care-AI](https://github.com/samiullah156-creator/Cotton-Care-AI) web app.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white) ![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white) ![Keras](https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white)

## Features

- REST endpoint that takes a leaf image and returns the predicted disease class with confidence
- CNN trained on cotton leaf images (training notebook included in `my_models/`)
- Ready for Heroku-style deployment with a `Procfile`

## Tech stack

- Python, Flask
- TensorFlow / Keras
- Jupyter for model training

## Getting started

```bash
python -m venv venv
# Windows: venv\Scripts\activate   macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
python app.py
```

## Author

**Ch Muhammad Samiullah**, AI Automation Engineer and Full-Stack Developer.
[GitHub](https://github.com/samiullah156-creator) · [Lexvaxa](https://lexvaxa.com)
