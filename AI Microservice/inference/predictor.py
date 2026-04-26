
MODEL_VERSION = "MedVision-1.0"
PNEUMONIA_THRESHOLD=0.75

import base64
import torch
import os
import cv2
import numpy as np
from PIL import Image
from torchvision import transforms

from models.densenet_model import DenseNetModel
from explainability.gradcam import GradCAM,overlay_heatmap
from training import config

class MedVisionPredictor:
  def __init__(self):
    self.device=torch.device(
        "cuda" if torch.cuda.is_available() else "cpu"
    )

    self.model=DenseNetModel().to(self.device)

    self.model.load_state_dict(
        torch.load(
            os.path.join(config.CHECKPOINT_DIR,"best_model.pth"),
            map_location=self.device
        )
    )

    self.model.eval()

    target_layer=self.model.backbone.features
    self.gradcam=GradCAM(self.model,target_layer)

    self.transform=transforms.Compose([
        transforms.Resize((224,224)),
        transforms.ToTensor(),
        transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
        ])

    self.classes=["NORMAL","PNEUMONIA"]

    

  def predict(self,image_path):
    image=Image.open(image_path).convert("RGB")

    input_tensor=self.transform(image)\
    .unsqueeze(0)\
    .to(self.device)

    input_tensor.requires_grad=True

    #with torch.no_grad():
    output=self.model(input_tensor)
    prob=torch.sigmoid(output).item()

    label=self.classes[int(prob>PNEUMONIA_THRESHOLD)]

    cam=self.gradcam.generate(input_tensor)

    original=np.array(image.resize((224,224)))/225.0
    result=overlay_heatmap(original,cam)

    heatmap_path="temp_heatmap.jpg"

    cv2.imwrite(
        heatmap_path,
        cv2.cvtColor(result,cv2.COLOR_RGB2BGR)
    )

    with open(heatmap_path, "rb") as img:
      encoded_image=base64.b64encode(img.read()).decode("utf-8")

    return{
          "prediction":label,
          "confidence":float(prob),
          "model_version":MODEL_VERSION,
          "heatmap_image":encoded_image,
    }

