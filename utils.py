from PIL import Image


ALLOWED_FORMATS = [
    "JPEG",
    "PNG",
    "WEBP"
]

MAX_FILE_SIZE = 10 * 1024 * 1024


def validate_image(uploaded_file):
    """
    Validate file size and image format.
    """

    if uploaded_file.size > MAX_FILE_SIZE:
        return False, "File size is larger than 10 MB."

    try:
        image = Image.open(uploaded_file)

        if image.format not in ALLOWED_FORMATS:
            return False, "Unsupported image format."

        image.verify()

    except Exception:
        return False, "Invalid or corrupted image."

    return True, "Valid image."


def get_image_info(image):
    """
    Return basic information about an image.
    """

    return {
        "width": image.width,
        "height": image.height,
        "format": image.format
    }