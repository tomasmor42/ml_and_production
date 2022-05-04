import base64
import cv2
import numpy as np

async def build(image, model_path, scale_coeff):
    content = await image.read()
    cv2_image = cv2.cvtColor(np.frombuffer(content, np.uint8), cv2.COLOR_BGR2RGB)
    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    sr.readModel(model_path)
    sr.setModel("EDSR", scale_coeff)
    res = sr.upsample(cv2_image)
    res = base64.b64encode(res)
    return res
