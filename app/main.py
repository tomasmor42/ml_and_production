import os
from os.path import exists
import numpy as np
import cv2
from typing import Optional
from fastapi import FastAPI, Header, UploadFile, HTTPException
from build import build

app = FastAPI()
path_to_models = os.getenv("MODELS_PATH", "/code/app/models/EDSR_Tensorflow/models/")

@app.post("/forward")
async def create_upload_file(image: UploadFile, scaleCoeff: Optional[int] = Header(None)):
    if not scaleCoeff: 
        return HTTPException(status_code=400, detail="Bad request")
    model_path = path_to_models + f"EDSR_x{str(scaleCoeff)}.pb"
    if not exists(model_path):
        return HTTPException(status_code=404, detail="Model doesn't exist")
    res = await build(image, model_path, scaleCoeff)
    return {"res": res.decode('utf-8')}
