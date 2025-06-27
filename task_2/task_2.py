import cv2
import numpy as np

def task_1(image):
    pixel = image[0, 0]
    b, g, r = pixel
    print(f"[Task 1] Top-left pixel (B, G, R): {b}, {g}, {r}")

def task_2(image):
    modified = image.copy()
    h, w = modified.shape[:2]
    print("[Task 2] Displaying original image...")
    cv2.imshow("Task 2 - Original", image)
    modified[h-1, w-1] = (0, 0, 255)
    print("[Task 2] Displaying modified image with bottom-right pixel set to red.")
    cv2.imshow("Task 2 - Modified", modified)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def task_3(image):
    h, w = image.shape[:2]
    cx, cy = w // 2, h // 2
    center_pixel = image[cy, cx]
    print(f"[Task 3] Image center: ({cx}, {cy}), Pixel value (B, G, R): {center_pixel}")

def task_4(image):
    modified = image.copy()
    h, w = modified.shape[:2]
    x = int(input("[Task 4] Enter X coordinate: "))
    y = int(input("[Task 4] Enter Y coordinate: "))
    if 0 <= x < w and 0 <= y < h:
        modified[y, x] = (0, 0, 0)
        print(f"[Task 4] Set pixel at ({x},{y}) to black.")
        cv2.imshow("Task 4", modified)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("[Task 4] Coordinates out of image bounds.")

def task_5(image):
    modified = image.copy()
    h, w = modified.shape[:2]
    modified[0:h//2, 0:w//2] = (255, 0, 0)
    print("[Task 5] Top-left quarter filled with blue.")
    cv2.imshow("Task 5", modified)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def task_6(image):
    modified = image.copy()
    h, w = modified.shape[:2]
    cx, cy = w // 2, h // 2
    half = 50
    modified[cy-half:cy+half, cx-half:cx+half] = (0, 0, 255)
    print("[Task 6] 100x100 square centered filled with red.")
    cv2.imshow("Task 6", modified)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def task_7(image):
    h, w = image.shape[:2]
    dh, dw = h // 3, w // 3
    center_crop = image[dh:2*dh, dw:2*dw]
    print("[Task 7] Displaying center region of 9-part grid.")
    cv2.imshow("Task 7 - Center Crop", center_crop)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def task_8(image):
    modified = image.copy()
    h = modified.shape[0]
    print("[Task 8] Displaying original image...")
    cv2.imshow("Task 8 - Original", image)
    if h > 100:
        modified[100, :] = (0, 255, 0)
        print("[Task 8] Row 100 set to green.")
    else:
        print("[Task 8] Image too small to modify row 100.")
    cv2.imshow("Task 8 - Modified", modified)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def task_9(image):
    modified = image.copy()
    print("[Task 9] Displaying original image...")
    cv2.imshow("Task 9 - Original", image)
    modified[50:100, 50:100] = (255, 255, 255)
    print("[Task 9] Region (50,50)-(100,100) set to white.")
    cv2.imshow("Task 9 - Modified", modified)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def task_10(image):
    pixel1 = image[50, 50]
    pixel2 = image[200, 200] if image.shape[0] > 200 and image.shape[1] > 200 else image[-1, -1]
    diff = np.abs(pixel1.astype(int) - pixel2.astype(int))
    print(f"[Task 10] Pixel at (50,50): {pixel1}, Pixel at (200,200): {pixel2}")
    print(f"[Task 10] Difference (B, G, R): {diff}")

def task_11(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(gray)
    print(f"[Task 11] Brightest pixel at {max_loc} with brightness {max_val}")

image_path = "data/dog.jpeg"
image = cv2.imread(image_path)

if image is None:
    print("Error: Could not load image.")
else:
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
    task_11(image)