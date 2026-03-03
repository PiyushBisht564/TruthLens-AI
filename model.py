import torch
from transformers import AutoImageProcessor, AutoModelForImageClassification
from PIL import Image
import io

# ----------------------------
# CONFIG
# ----------------------------
MODEL_NAME = "dima806/deepfake_vs_real_image_detection"
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Lower threshold because of concept drift
FAKE_THRESHOLD = 0.1  

# ----------------------------
# LOAD MODEL (only once)
# ----------------------------
processor = AutoImageProcessor.from_pretrained(MODEL_NAME)
model = AutoModelForImageClassification.from_pretrained(MODEL_NAME)

model.to(DEVICE)
model.eval()


# ----------------------------
# PREDICTION FUNCTION
# ----------------------------
def predict_image(image_bytes):

    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    inputs = processor(images=image, return_tensors="pt").to(DEVICE)

    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probs = torch.softmax(logits, dim=1)

    # Get fake probability
    fake_index = model.config.label2id["Fake"]
    fake_probability = probs[0][fake_index].item()

    # Apply threshold
    if fake_probability > FAKE_THRESHOLD:
        label = "FAKE"
        confidence = fake_probability
    else:
        label = "REAL"
        confidence = 1 - fake_probability

    return label, fake_probability, confidence