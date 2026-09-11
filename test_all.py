from pathlib import Path
from PIL import Image
from processor import remove_background

TEST_FOLDER = Path("tests")
OUTPUT_FOLDER = TEST_FOLDER / "results"

OUTPUT_FOLDER.mkdir(exist_ok=True)

images = list(TEST_FOLDER.glob("*.jpg"))

if not images:
    print("No JPG images found in the tests folder.")
else:
    for image_path in images:
        print(f"\nProcessing: {image_path.name}")

        try:
            image = Image.open(image_path)

            output, processing_time = remove_background(image)

            output_path = OUTPUT_FOLDER / f"{image_path.stem}_output.png"
            output.save(output_path)

            print(f"Success!")
            print(f"Processing time: {processing_time:.2f} seconds")
            print(f"Output: {output_path}")

        except Exception as e:
            print(f"Error: {e}")

print("\nAll tests completed!")