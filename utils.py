from PIL import Image


ALLOWED_FORMATS = ["JPEG","PNG","WEBP"]

MAX_FILE_SIZE = 10 * 1024 * 1024


def validate_image(uploaded_file):
    try:
        # Read file data to determine size
        uploaded_file.seek(0)
        file_data = uploaded_file.read()
        file_size = len(file_data)

        # Check file size
        if file_size > MAX_FILE_SIZE:
            return False, "File size is larger than 10 MB."

        # Reset file position
        uploaded_file.seek(0)

        # Open image
        image = Image.open(uploaded_file)

        # Check image format
        if image.format not in ALLOWED_FORMATS:
            return False, "Unsupported image format."

        # Verify image integrity
        image.verify()

        # Reset file position again
        uploaded_file.seek(0)

        return True, "Valid image."

    except Exception:
        uploaded_file.seek(0)
        return False, "Invalid or corrupted image."


def get_image_info(image):
    
    #Return basic information about an image.
    return {
        "width": image.width,
        "height": image.height,
        "format": image.format
    }