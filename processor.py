from rembg import remove
from PIL import Image
import io
import time


MAX_DIMENSION = 2500


def resize_image(image):
    """
    Resize large images while maintaining their aspect ratio.
    """

    image = image.copy()

    if max(image.size) > MAX_DIMENSION:
        ratio = MAX_DIMENSION / max(image.size)

        new_width = int(image.width * ratio)
        new_height = int(image.height * ratio)

        image = image.resize(
            (new_width, new_height),
            Image.Resampling.LANCZOS
        )

    return image


def remove_background(image):
    """
    Remove the background from an image using rembg.
    Returns the processed image and processing time.
    """

    image = resize_image(image)

    start_time = time.perf_counter()

    output = remove(image)

    end_time = time.perf_counter()

    processing_time = end_time - start_time

    return output, processing_time


def image_to_bytes(image):
    """
    Convert a PIL image into PNG bytes.
    """

    buffer = io.BytesIO()

    image.save(
        buffer,
        format="PNG"
    )

    buffer.seek(0)

    return buffer.getvalue()