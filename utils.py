from PIL import Image


ALLOWED_FORMATS = ["JPEG","PNG","WEBP"]

MAX_FILE_SIZE = 10 * 1024 * 1024


def validate_image(uploaded_file):
    try:
        # Check file size
        if uploaded_file.size > MAX_FILE_SIZE:
            return False, "File size is larger than 10 MB."

        # Check file format using filename
        file_extension = uploaded_file.name.lower().split(".")[-1]

        if file_extension not in ["jpg", "jpeg", "png", "webp"]:
            return False, "Unsupported image format."

        return True, "Valid image."

    except Exception as e:
        return False, f"Image validation error: {str(e)}"


def get_image_info(image):
    
    #Return basic information about an image.
    return {
        "width": image.width,
        "height": image.height,
        "format": image.format
    }