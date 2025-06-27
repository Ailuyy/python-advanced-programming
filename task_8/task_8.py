import cv2

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
    roi = image[0:100, 0:100]
    show_image("Top-left 100x100 ROI", roi)

def task_2(image):
    (h, _) = image.shape[:2]
    roi = image[h//2:, :]
    show_image("Bottom Half", roi)

def task_3(image):
    (_, w) = image.shape[:2]
    roi = image[:, w//2:]
    show_image("Right Half", roi)

def task_4(image):
    try:
        startX = int(input("startX: "))
        endX = int(input("endX: "))
        startY = int(input("startY: "))
        endY = int(input("endY: "))
    except ValueError:
        print("Niepoprawne dane wejściowe.")
        return
    roi = image[startY:endY, startX:endX]
    show_image("User-defined ROI", roi)

def task_5(image):
    (h, w) = image.shape[:2]
    centerY, centerX = h//2, w//2
    roi = image[centerY-75:centerY+75, centerX-75:centerX+75]
    show_image("Cropped Face Region (centered)", roi)

def task_6(image):
    roi = image[50:150, 50:150]
    result = image.copy()
    result[0:100, 0:100] = roi
    show_image("Copied and Pasted ROI", result)

def task_7(image):
    (h, w) = image.shape[:2]
    dh, dw = h // 3, w // 3
    for row in range(3):
        for col in range(3):
            roi = image[row*dh:(row+1)*dh, col*dw:(col+1)*dw]
            show_image(f"Grid {row},{col}", roi)

def task_8(image):
    (h, w) = image.shape[:2]
    win_w = 200
    for x in range(0, w - win_w + 1, 10):
        roi = image[0:h, x:x+win_w]
        cv2.imshow("Sliding ROI", roi)
    cv2.waitKey(5)
    cv2.destroyAllWindows()

def task_9(image):
    roi = image[0:300, 0:300]
    cv2.imwrite("cropped_image.jpg", roi)
    print("Zapisano jako cropped_image.jpg")
    show_image("Cropped 300x300", roi)


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
