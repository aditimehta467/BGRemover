from PIL import Image
from processor import remove_background


input_image = Image.open("test.jpg")

output_image, processing_time = remove_background(input_image)

output_image.save("test_output.png")

print("Background removed successfully!")
print(f"Processing time: {processing_time:.2f} seconds")