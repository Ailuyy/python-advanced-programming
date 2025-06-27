import cv2
import numpy as np
import imutils

def load_image(path):
    image = cv2.imread(path)
    if image is None:
        raise ValueError(f"Nie można wczytać obrazu: {path}")
    return image

def show_image(title, image):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def task_1(image):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, 45, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    show_image("Original", image)
    show_image("Rotated by 45 Degrees", rotated)

def task_2(image):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, -90, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    show_image("Rotated by -90 Degrees", rotated)

def task_3(image):
    (h, w) = image.shape[:2]
    M = cv2.getRotationMatrix2D((0, 0), 30, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    show_image("Rotated around (0, 0) by 30 Degrees", rotated)

def task_4(image):
    angle = float(input("Podaj kąt obrotu: "))
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    show_image(f"Rotated by {angle} Degrees", rotated)

def task_5(image):
    rotated = imutils.rotate(image, 180)
    show_image("Rotated by 180 Degrees (imutils.rotate)", rotated)

def task_6(image):
    rotated = imutils.rotate_bound(image, -33)
    show_image("Rotated by -33 Degrees (rotate_bound)", rotated)

def task_7(image):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, 60, 1.0)
    rotated_cv2 = cv2.warpAffine(image, M, (w, h))
    rotated_imutils = imutils.rotate(image, -60)
    show_image("Rotated by 60 Degrees (cv2.warpAffine)", rotated_cv2)
    show_image("Rotated by 60 Degrees (imutils.rotate)", rotated_imutils)

def task_8(image):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    rotated = image.copy()
    for _ in range(3):
        M = cv2.getRotationMatrix2D(center, 30, 1.0)
        rotated = cv2.warpAffine(rotated, M, (w, h))
    show_image("3x 30 Degrees Rotation", rotated)

    M90 = cv2.getRotationMatrix2D(center, 90, 1.0)
    rotated90 = cv2.warpAffine(image, M90, (w, h))
    show_image("Single 90 Degrees Rotation", rotated90)

def task_9(image):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, 75, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    cv2.imwrite("rotated_output.jpg", rotated)
    print("Zapisano obraz jako rotated_output.jpg")
    show_image("Rotated and Saved", rotated)

def task_10(image):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    for angle in range(0, 361, 15):
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv2.warpAffine(image, M, (w, h))
        cv2.imshow(f"Rotation {angle} Degrees", rotated)
        cv2.waitKey(500)
    cv2.destroyAllWindows()


image = load_image("data/dog.jpeg")
task_1(image)
task_2(image)
task_3(image)
task_4(image)
task_5(image)
task_6(image)
task_7(image)
task_8(image)
task_9(image)
task_10(image)
