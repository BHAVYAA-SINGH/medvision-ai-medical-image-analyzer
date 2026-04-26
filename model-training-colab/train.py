import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import torch
import torch.nn as nn
from tqdm import tqdm
import os

from training import config
from utils.dataset import get_dataloaders
from models.densenet_model import build_model

#======================================
#LOSS FUNCTION
#========================================
def get_loss_function():
  if config.LOSS_FUNCTION=="bce":
    return nn.BCEWithLogitsLoss()
  else:
    raise ValueError("Unsupported loss function")
#=========================================
#OPTIMIZER
#==========================================
def get_optimizer(model):
  if config.OPTIMIZER=="adam":
    return torch.optim.Adam(
        model.parameters(),
        lr=config.LEARNING_RATE
    )
  else:
    raise ValueError("Unsupported optimizer")
#===========================================
#TRAINING STEPS
#===========================================
def train_one_epoch(model,loader,criterion,optimizer):
  model.train()
  running_loss=0.0

  for images, labels in tqdm(loader):
    images=images.to(config.DEVICE)
    labels=labels.float().unsqueeze(1).to(config.DEVICE)

    #FORWARD
    outputs=model(images)
    loss=criterion(outputs,labels)

    #BACKDROP
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    running_loss+=loss.item()

  return running_loss/len(loader)

def validate(model,loader,criterion):
  model.eval()
  running_loss=0.0

  with torch.no_grad():
    for images, labels in loader:
      images=images.to(config.DEVICE)
      labels=labels.float().unsqueeze(1).to(config.DEVICE)

      outputs=model(images)
      loss=criterion(outputs,labels)

      running_loss+=loss.item()

  return running_loss/len(loader)


  #============================================
  #MAIN EXECUTION
  #============================================
def train():
  train_loader, val_loader,_=get_dataloaders()

  model=build_model()
  criterion=get_loss_function()
  optimizer=get_optimizer(model)

  best_val_loss=float("inf")
  os.makedirs(config.CHECKPOINT_DIR,exist_ok=True)

  for epoch in range(config.EPOCHS):
    print(f"\nEpoch [{epoch+1}/{config.EPOCHS}]")

    train_loss=train_one_epoch(
        model,train_loader,criterion,optimizer
        )

    val_loss=validate(
        model,val_loader,criterion
        )

    print(f"Train Loss:{train_loss:.4f}")
    print(f"Val Loss: {val_loss:.4f}")

    #Save best model
    if val_loss < best_val_loss:
      best_val_loss=val_loss

      torch.save(
          model.state_dict(),
          os.path.join(config.CHECKPOINT_DIR,"best_model.pth")
          )

      print("Best model saved!")


if __name__ == "__main__":
    train()

