from fastapi import FastAPI, UploadFile, File
import shutil
import uuid
import os

from inference.predictor import MedVisionPredictor

app=FastAPI(title="MedVision AI Service")

predictor=MedVisionPredictor()

@app.post("/predict")
async def predict(file: UploadFile = File(...)):

  try:

    temp_path=f"temp_{uuid.uuid4()}.jpg"
    with open(temp_path,"wb") as buffer:
      shutil.copyfileobj(file.file,buffer)

    result=predictor.predict(temp_path)
    os.remove(temp_path)

    return result

  except Exception as e:
    return {"error": str(e)}
      
