import torch
import os
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from tqdm import tqdm

from models.densenet_model import DenseNetModel
from utils.dataset import get_dataloaders
from training import config

def validate():
  device=torch.device("cuda"if torch.cuda.is_available() else "cpu")

  #Load data
  _, val_loader, test_loader = get_dataloaders()
  loader = test_loader if test_loader else val_loader

  #Load model
  model=DenseNetModel().to(device)
  model.load_state_dict(torch.load(os.path.join(config.CHECKPOINT_DIR,"best_model.pth")))
  model.eval()

  all_preds=[]
  all_labels=[]
  all_probs=[]

  with torch.no_grad():
    for images, labels in tqdm(loader):
      images=images.to(device)
      labels=labels.float().unsqueeze(1).to(device)

      outputs=model(images)
      probs=torch.sigmoid(outputs)

      preds=(probs>0.5).float()

      all_probs.extend(probs.cpu().numpy())
      all_preds.extend(preds.cpu().numpy())
      all_labels.extend(labels.cpu().numpy())

  #Metrics
  acc=accuracy_score(all_labels,all_preds)
  precision=precision_score(all_labels,all_preds)
  recall=recall_score(all_labels,all_preds)
  f1=f1_score(all_labels,all_preds)

  try:
    auc=roc_auc_score(all_labels,all_probs)
  except:
    auc=0

  print("\n===== Evaluation Results =====")
  print(f"Accuracy : {acc:.4f}")
  print(f"Precision : {precision:.4f}")
  print(f"Recall : {recall:.4f}")
  print(f"F1 Score : {f1:.4f}")
  print(f"ROC-AOC : {auc:.4f}")

if __name__ == "__main__":
  validate()
