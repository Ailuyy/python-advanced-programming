import cv2
import numpy as np

def task_1(image):
    cv2.imshow("Task 1 - Original", image)
    M = np.float32([[1, 0, 30], [0, 1, 40]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    cv2.imshow("Task 1 - Shifted Right 30px, Down 40px", shifted)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def task_2(image):
    M = np.float32([[1, 0, -20], [0, 1, -50]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    cv2.imshow("Task 2 - Shifted Left 20px, Up 50px", shifted)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def task_3(image):
    tx = -image.shape[1] // 2 - 10
    ty = -image.shape[0] // 2 - 10
    M = np.float32([[1, 0, tx], [0, 1, ty]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    cv2.imshow("Task 3 - Shifted Beyond Half Image", shifted)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def task_4(image):
    try:
        import imutils
    except ImportError:
        print("Task 4: imutils not installed. Run 'pip install imutils'")
        return

    shifted_cv2 = cv2.warpAffine(image, np.float32([[1, 0, 100], [0, 1, 50]]), (image.shape[1], image.shape[0]))
    shifted_imutils = imutils.translate(image, 100, 50)

    cv2.imshow("Task 4 - cv2.warpAffine", shifted_cv2)
    cv2.imshow("Task 4 - imutils.translate", shifted_imutils)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def task_5(image):
    try:
        tx = int(input("Task 5 - Enter horizontal shift (tx): "))
        ty = int(input("Task 5 - Enter vertical shift (ty): "))
    except ValueError:
        print("Invalid input. Please enter integer values.")
        return

    M = np.float32([[1, 0, tx], [0, 1, ty]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    cv2.imshow(f"Task 5 - Shifted by tx={tx}, ty={ty}", shifted)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image = cv2.imread("data/dog.jpeg")

task_1(image)
task_2(image)
task_3(image)
task_4(image)
task_5(image)