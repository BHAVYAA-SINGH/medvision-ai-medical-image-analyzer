import torch
import torch.nn as nn
import torchvision.models as models

from training import config

# def disable_inplace_relu(module):
#   for child in module.children():
#     if isinstance(child,torch.nn.ReLU):
#       child.inplace=False
#     else:
#       disable_inplace_relu(child)

class DenseNetModel(nn.Module):
  def __init__(self):
    super(DenseNetModel,self).__init__()

    self.backbone=models.densenet121(weights="IMAGENET1K_V1")
    # disable_inplace_relu(self.backbone)

    for param in self.backbone.features.parameters():
      param.requires_grad=False

    num_features=self.backbone.classifier.in_features

    self.backbone.classifier=nn.Sequential(
        nn.Linear(num_features,256),
        nn.ReLU(),
        nn.Dropout(0.5),
        nn.Linear(256,config.NUM_CLASSES)
    )

  def forward(self,x):
    return self.backbone(x)

def build_model():
  model=DenseNetModel()
  return model.to(config.DEVICE)
