import cv2

def task_1(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print(f"[Task 1] Error: Image not found at path: {image_path}")
        return None
    print("[Task 1] Image loaded successfully.")
    cv2.imshow("Task 1: Original Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return image

def task_2(image):
    if image is None:
        print("[Task 2] No input image.")
        return
    height, width, channels = image.shape
    print(f"[Task 2] Dimensions: {width}x{height}, Channels: {channels}")

def task_3(image_path):
    gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if gray_image is None:
        print("[Task 3] Error: Could not load grayscale image.")
        return None
    cv2.imshow("Task 3: Grayscale Image", gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("[Task 3] Channels: 1 (grayscale)")
    return gray_image

def task_4(gray_image, save_path="gray_output.jpg"):
    if gray_image is None:
        print("[Task 4] No grayscale image to save.")
        return
    success = cv2.imwrite(save_path, gray_image)
    if success:
        print(f"[Task 4] Image saved as '{save_path}'.")
    else:
        print("[Task 4] Error saving image.")

def task_5(image_path1, image_path2):
    image1 = cv2.imread(image_path1)
    image2 = cv2.imread(image_path2)

    if image1 is None or image2 is None:
        print("[Task 5] Error: One or both images could not be loaded.")
        return

    cv2.imshow("Task 5: Image 1", image1)
    cv2.imshow("Task 5: Image 2", image2)
    print("[Task 5] Press any key to close both images.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def task_6(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("[Task 6] Error: Could not load image.")
        return
    cv2.namedWindow("Task 6: Resizable Window", cv2.WINDOW_NORMAL)
    cv2.imshow("Task 6: Resizable Window", image)
    print("[Task 6] Window should be resizable.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_path = "data/dog.jpeg"
second_image_path = "data/ruby.jpeg"

image = task_1(image_path)
task_2(image)
gray_image = task_3(image_path)
task_4(gray_image)
task_5(image_path, second_image_path)
task_6(image_path)
