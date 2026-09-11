BGRemover – AI Background Remover

BGRemover is a small image background removal tool built using Python and Streamlit. 
I built this project to understand how image processing and pretrained computer 
vision models can be used in a practical application.

The application takes an uploaded image, detects the main subject, removes the 
background, and provides the result as a transparent PNG.

Live Demo

[Try BGRemover](https://bgremover-jrcqieeijhufl59vcpxm57.streamlit.app/)

Features

- Upload JPG, JPEG, PNG, or WEBP images
- Automatically remove the image background
- Preview the original and processed image
- Download the result as a PNG
- Supports transparent backgrounds
- Basic image validation
- Handles different image sizes
- Simple web interface using Streamlit

How it works

The main background removal is handled by the `rembg` library, which uses a 
pretrained U²-Net model for foreground/background segmentation.

The basic workflow is:

1. Upload an image.
2. Validate the uploaded file.
3. Pass the image to the background removal model.
4. Generate an image with the background removed.
5. Display the original and processed images.
6. Download the final PNG.

Technologies Used

- Python – Main programming language
- Streamlit – Web application interface
- rembg – Background removal
- U²-Net** – Pretrained image segmentation model
- Pillow (PIL) – Image processing
- ONNX Runtime – Model inference
- Streamlit Community Cloud – Deployment

