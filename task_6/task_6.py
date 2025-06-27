import cv2
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
    resized = cv2.resize(image, (image.shape[1] // 2, image.shape[0] // 2), interpolation=cv2.INTER_AREA)
    show_image("Resized 50%", resized)

def task_2(image):
    resized = cv2.resize(image, (image.shape[1] * 2, image.shape[0] * 2), interpolation=cv2.INTER_LINEAR)
    show_image("Resized 200% (INTER_LINEAR)", resized)

def task_3(image):
    resized = cv2.resize(image, (200, 300))
    show_image("Resized to 200x300", resized)

def task_4(image):
    methods = [
        ("cv2.INTER_NEAREST", cv2.INTER_NEAREST),
        ("cv2.INTER_LINEAR", cv2.INTER_LINEAR),
        ("cv2.INTER_CUBIC", cv2.INTER_CUBIC),
        ("cv2.INTER_LANCZOS4", cv2.INTER_LANCZOS4)
    ]
    for (name, method) in methods:
        resized = imutils.resize(image, width=image.shape[1] * 3, inter=method)
        print(f"[INFO] {name}")
        show_image(f"Interpolation: {name}", resized)

def task_5(image):
    resized = imutils.resize(image, width=500)
    show_image("Resized to width 500 (keep aspect)", resized)

def task_6(image):
    resized = imutils.resize(image, height=400)
    show_image("Resized to height 400 (keep aspect)", resized)

def task_7(image):
    methods = [
        ("INTER_AREA", cv2.INTER_AREA),
        ("INTER_LINEAR", cv2.INTER_LINEAR),
        ("INTER_NEAREST", cv2.INTER_NEAREST)
    ]
    for (name, method) in methods:
        resized = cv2.resize(image, (image.shape[1] // 5, image.shape[0] // 5), interpolation=method)
        print(f"[INFO] Downscale using {name}")
        show_image(f"Downscaled 5x ({name})", resized)

def task_8(image):
    methods = [
        ("INTER_CUBIC", cv2.INTER_CUBIC),
        ("INTER_LANCZOS4", cv2.INTER_LANCZOS4)
    ]
    for (name, method) in methods:
        resized = cv2.resize(image, (image.shape[1] * 4, image.shape[0] * 4), interpolation=method)
        print(f"[INFO] Upscale using {name}")
        show_image(f"Upscaled 4x ({name})", resized)

def task_9(image):
    for scale in range(100, 301, 20):
        width = int(image.shape[1] * scale / 100)
        height = int(image.shape[0] * scale / 100)
        resized = cv2.resize(image, (width, height))
        cv2.imshow(f"Scaled to {scale}%", resized)
        cv2.waitKey(500)
    cv2.destroyAllWindows()

def task_10(image):
    resized = imutils.resize(image, width=800)
    cv2.imwrite("resized_output.jpg", resized)
    print("Zapisano obraz jako resized_output.jpg")
    show_image("Saved resized image", resized)


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