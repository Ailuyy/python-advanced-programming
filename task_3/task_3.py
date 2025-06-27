import cv2
import numpy as np

def task_1():
    image = np.zeros((300, 300, 3), dtype="uint8")
    h, w = image.shape[:2]
    blue = (255, 0, 0)
    cv2.line(image, (w // 2, h // 2), (w, h), blue, 2)
    cv2.imshow("Task 1", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def task_2():
    image = np.zeros((400, 400, 3), dtype="uint8")
    green = (0, 255, 0)
    red = (0, 0, 255)
    cv2.rectangle(image, (0, 0), (100, 50), green, -1)
    cv2.rectangle(image, (300, 350), (400, 400), red, 3)
    cv2.imshow("Task 2", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def task_3():
    image = np.zeros((300, 300, 3), dtype="uint8")
    blue = (255, 0, 0)
    red = (0, 0, 255)
    cv2.circle(image, (40, 40), 40, blue, -1)
    center = (image.shape[1] // 2, image.shape[0] // 2)
    cv2.circle(image, center, 60, red, -1)
    cv2.imshow("Task 3", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def task_4():
    image = np.zeros((300, 300, 3), dtype="uint8")
    square_size = 100
    circle_radius = 30
    center = (image.shape[1] // 2, image.shape[0] // 2)
    top_left = (center[0] - square_size // 2, center[1] - square_size // 2)
    bottom_right = (center[0] + square_size // 2, center[1] + square_size // 2)
    cv2.rectangle(image, top_left, bottom_right, (255, 255, 255), 2)
    cv2.circle(image, center, circle_radius, (255, 0, 0), 2)
    cv2.imshow("Task 4", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def task_5():
    image = np.zeros((300, 300, 3), dtype="uint8")
    center = (image.shape[1] // 2, image.shape[0] // 2)
    for size in range(20, 201, 20):
        top_left = (center[0] - size // 2, center[1] - size // 2)
        bottom_right = (center[0] + size // 2, center[1] + size // 2)
        cv2.rectangle(image, top_left, bottom_right, (255, 255, 255), 1)
    cv2.imshow("Task 5", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def task_6(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Task 6: Error loading image.")
        return
    red = (0, 0, 255)
    green = (0, 255, 0)
    blue = (255, 0, 0)

    left_eye = (560, 360)
    right_eye = (690, 380)
    eye_radius = 30

    mouth_top_left = (530, 480)
    mouth_bottom_right = (700, 500)

    face_center = (600, 440)
    face_radius = 200

    cv2.circle(image, left_eye, eye_radius, red, -1)
    cv2.circle(image, right_eye, eye_radius, red, -1)
    cv2.rectangle(image, mouth_top_left, mouth_bottom_right, green, -1)
    cv2.circle(image, face_center, face_radius, blue, 3)

    cv2.imshow("Task 6 - Face Masking", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

task_1()
task_2()
task_3()
task_4()
task_5()
task_6("data/face.jpeg")
