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
    flipped = cv2.flip(image, 1)
    show_image("Flipped Horizontally", flipped)

def task_2(image):
    flipped = cv2.flip(image, 0)
    show_image("Original", image)
    show_image("Flipped Vertically", flipped)

def task_3(image):
    flipped = cv2.flip(image, -1)
    show_image("Flipped Horizontally & Vertically", flipped)

def task_4(image):
    flipped_h = cv2.flip(image, 1)
    flipped_v = cv2.flip(image, 0)
    flipped_both = cv2.flip(image, -1)
    show_image("Original", image)
    show_image("Flipped Horizontally", flipped_h)
    show_image("Flipped Vertically", flipped_v)
    show_image("Flipped Both Axes", flipped_both)

def task_5(image):
    (h, w) = image.shape[:2]
    roi = image[:, w//2:]
    flipped_roi = cv2.flip(roi, 1)
    result = image.copy()
    result[:, w//2:] = flipped_roi
    show_image("Flipped Right Half Only", result)

def task_6(image):
    try:
        flip_code = int(input("Wybierz sposób odbicia (0 – pionowe, 1 – poziome, -1 – oba): "))
        if flip_code not in [0, 1, -1]:
            print("Nieprawidłowy wybór. Dozwolone wartości to 0, 1 lub -1.")
            return
    except ValueError:
        print("Błąd: podano nieprawidłową wartość.")
        return
    flipped = cv2.flip(image, flip_code)
    show_image(f"Flipped (code={flip_code})", flipped)

image = load_image("data/dog.jpeg")
task_1(image)
task_2(image)
task_3(image)
task_4(image)
task_5(image)
task_6(image)