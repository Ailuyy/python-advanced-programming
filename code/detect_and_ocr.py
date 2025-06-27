import os
import time
import cv2
import random
from fast_alpr import ALPR
from parse_annotation import parse_annotation

alpr = ALPR(ocr_model='european-plates-mobile-vit-v2-model',
            detector_model='yolo-v9-t-384-license-plate-end2end')

def detect_and_ocr(img_dir: str, max_images: int = 0, visualize: bool = False):
    files = [f for f in os.listdir(img_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    if not files:
        return [], 0.0

    if max_images and len(files) > max_images:
        files = random.sample(files, max_images)

    gt_texts = {f: parse_annotation(f)[1] for f in files}
    results = []
    t0 = time.time()

    for fname in files:
        path = os.path.join(img_dir, fname)
        image = cv2.imread(path)
        if image is None:
            continue
        gt = gt_texts[fname]

        detections = alpr.detector.predict(image)

        if not detections:
            results.append({'file': fname, 'gt_text': gt, 'pred_text': '', 'ocr_ok': False})
            continue

        best_text = ''
        best_conf = 0.0

        for det in detections:
            box = det.bounding_box
            y1, y2 = max(0, box.y1), min(image.shape[0], box.y2)
            x1, x2 = max(0, box.x1), min(image.shape[1], box.x2)
            if y1 >= y2 or x1 >= x2:
                continue

            crop = image[y1:y2, x1:x2]
            ocr_out = alpr.ocr.predict(crop)

            if not ocr_out or not ocr_out.text:
                continue

            text = ocr_out.text.strip().upper().replace(" ", "")
            conf = ocr_out.confidence

            if conf > best_conf:
                best_text = text
                best_conf = conf

            if visualize:
                cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(image, text, (x1, max(0, y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        ok = best_text == gt.upper()
        print(f"[ALPR] PRED: '{best_text}' (conf: {best_conf:.2f}) | GT: '{gt}' | OK: {ok}")

        results.append({
            'file': fname,
            'gt_text': gt,
            'pred_text': best_text,
            'ocr_ok': ok
        })

        if visualize:
            cv2.imshow('alpr', crop)
            key = cv2.waitKey(0)

    if visualize:
        cv2.destroyAllWindows()

    return results, time.time() - t0