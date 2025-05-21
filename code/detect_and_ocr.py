import os
import time
import cv2
import easyocr
import random
import yolov5
from parse_annotation import parse_annotation

MODEL_NAME = 'keremberke/yolov5n-license-plate'
model  = yolov5.load(MODEL_NAME)
READER = easyocr.Reader(['en'])
model.conf = 0.25
model.iou  = 0.45

def detect_and_ocr(img_dir: str, max_images: int = 10, visualize: bool = False):
    files = [f for f in os.listdir(img_dir)
             if f.lower().endswith(('.jpg','.png'))]
    if not files:
        return [], 0.0

    if max_images and len(files) > max_images:
        files = random.sample(files, max_images)
    gt_texts = {f: parse_annotation(f)[1] for f in files}
    results = []
    t0 = time.time()

    for fname in files:
        path = os.path.join(img_dir, fname)
        orig = cv2.imread(path)
        if orig is None:
            continue
        gt = gt_texts[fname]

        h0, w0 = orig.shape[:2]
        scale  = 640 / w0 if w0 > 640 else 1.0
        small  = cv2.resize(orig, None, fx=scale, fy=scale,
                            interpolation=cv2.INTER_AREA)
        preds  = model(small).pred[0]
        if preds.shape[0] == 0:
            results.append({'file':fname,'gt_text':gt,
                            'pred_text':'','ocr_ok':False})
            continue

        best = preds[preds[:,4].argmax()]
        x1,y1,x2,y2 = map(int, best[:4].tolist())
        x1 = max(0, int(x1/scale));  y1 = max(0, int(y1/scale))
        x2 = min(w0, int(x2/scale)); y2 = min(h0, int(y2/scale))

        pad  = int(0.05 * max(y2-y1, x2-x1))
        crop = orig[
            max(0,   y1-pad):min(h0, y2+pad),
            max(0,   x1-pad):min(w0, x2+pad)
        ]

        gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
        _, bw = cv2.threshold(
            gray, 0, 255,
            cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
        )

        bw = cv2.resize(bw, None, fx=1.5, fy=1.5,
                        interpolation=cv2.INTER_LINEAR)

        texts = READER.readtext(
            bw,
            detail=0,
            allowlist='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ',
            text_threshold=0.4,
            low_text=0.3,
            mag_ratio=1.5
        )
        pred = max(texts, key=len).replace(' ','') if texts else ''

        ok = (pred.upper() == gt.upper())
        results.append({
            'file': fname,
            'gt_text': gt,
            'pred_text': pred,
            'ocr_ok': ok
        })

        if visualize:
            cv2.rectangle(crop, (pad,pad),
                          (crop.shape[1]-pad-1,crop.shape[0]-pad-1),
                          (0,255,0),2)
            cv2.imshow('plate', cv2.resize(
                crop, (800, int(800*crop.shape[0]/crop.shape[1]))
            ))
            cv2.waitKey(0)

    if visualize:
        cv2.destroyAllWindows()

    return results, time.time() - t0
