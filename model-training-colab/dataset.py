from torchvision import datasets,transforms
from torch.utils.data import DataLoader

from training import config
# ==============================
# IMAGE TRANSFORMS
# ==============================
train_transforms= transforms.Compose([
    transforms.Resize((config.IMAGE_SIZE,config.IMAGE_SIZE)),
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(10),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485,0.456,0.406],
        std=[0.229,0.224,0.225]
    )
])

val_test_transforms=transforms.Compose([
    transforms.Resize((config.IMAGE_SIZE,config.IMAGE_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485,0.456,0.406],
        std=[0.229,0.224,0.225]
    )
])
# ==============================
# DATASETS
# ==============================
train_dataset=datasets.ImageFolder(
    root=config.TRAIN_DIR,
    transform=train_transforms
)
val_dataset=datasets.ImageFolder(
    root=config.TRAIN_DIR,
    transform=val_test_transforms
)
test_dataset=datasets.ImageFolder(
    root=config.TEST_DIR,
    transform=val_test_transforms
)
# ==============================
# DATALOADERS
# ==============================
train_loader=DataLoader(
    train_dataset,
    batch_size=config.BATCH_SIZE,
    shuffle=True,
    num_workers=2,
    pin_memory=True
)
val_loader=DataLoader(
    val_dataset,
    batch_size=config.BATCH_SIZE,
    shuffle=False,
    num_workers=2,
    pin_memory=True
)
test_loader=DataLoader(
    test_dataset,
    batch_size=config.BATCH_SIZE,
    shuffle=False,
    num_workers=2,
    pin_memory=True
)
# ==============================
# GET LOADERS FUNCTION
# ==============================
def get_dataloaders():
  return train_loader,val_loader,test_loader
