import cv2
import numpy as np

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
    np_added = np.uint8(image + 50)
    cv_added = cv2.add(image, np.ones(image.shape, dtype="uint8") * 50)
    show_image("NumPy Added +50", np_added)
    show_image("OpenCV Added +50", cv_added)

def task_2(image):
    result_np = np.uint8(image + 150)
    result_cv = cv2.add(image, np.ones(image.shape, dtype="uint8") * 150)
    show_image("NumPy +150 (Burned)", result_np)
    show_image("OpenCV +150 (Clipped)", result_cv)

def task_3(image):
    result_np = np.uint8(image - 80)
    result_cv = cv2.subtract(image, np.ones(image.shape, dtype="uint8") * 80)
    show_image("NumPy -80 (Wrap) ", result_np)
    show_image("OpenCV -80 (Clip)", result_cv)

def task_4(image):
    b, g, r = cv2.split(image)
    r = cv2.add(r, 30)
    g = cv2.subtract(g, 20)
    b = cv2.add(b, 10)
    filtered = cv2.merge([b, g, r])
    show_image("Instagram-like Filter", filtered)


image = load_image("data/dog.jpeg")
task_1(image)
task_2(image)
task_3(image)
task_4(image)