import streamlit as st
from PIL import Image
from PIL import ImageColor
from processor import remove_background, image_to_bytes
from utils import validate_image

# PAGE CONFIGURATION
st.set_page_config(
    page_title="BGRemover - AI Background Remover",
    page_icon="🖼️",
    layout="wide"
)

# CUSTOM CSS
st.markdown(
    """
    <style>

    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .info-box {
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #ddd;
        margin-bottom: 20px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# HEADER
st.markdown(
    '<div class="main-title">🖼️ BGRemover</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'AI-powered image background remover'
    '</div>',
    unsafe_allow_html=True
)


st.write(
    "Upload an image and automatically remove its background "
    "using a pretrained computer vision model."
)

# SIDEBAR
with st.sidebar:

    st.header("⚙️ Settings")

    background_option = st.selectbox(
        "Background",
        [
            "Transparent",
            "White",
            "Black",
            "Custom Color"
        ]
    )

    custom_color = "#FFFFFF"

    if background_option == "Custom Color":

        custom_color = st.color_picker(
            "Pick a color",
            "#FFFFFF"
        )

    st.divider()

    st.write("### Supported formats")

    st.write(
        "JPG • JPEG • PNG • WEBP"
    )

    st.write("Maximum file size: 10 MB")

# FILE UPLOAD
uploaded_file = st.file_uploader(
    "Upload your image",
    type=["jpg","jpeg","png","webp"],
    accept_multiple_files=False
)


# PROCESS IMAGE
if uploaded_file is not None:

    # Validate file
    valid, message = validate_image(uploaded_file)

    if not valid:

        st.error(message)
        st.stop()

    # Open image
    uploaded_file.seek(0)

    input_image = Image.open(
        uploaded_file
    )

    # Convert image to RGB for processing
    if input_image.mode not in ["RGB", "RGBA"]:

        input_image = input_image.convert("RGB")

    # IMAGE INFORMATION
    st.subheader("Image Information")

    info_col1, info_col2, info_col3 = st.columns(3)

    with info_col1:
        st.metric(
            "Width",
            f"{input_image.width}px"
        )

    with info_col2:
        st.metric(
            "Height",
            f"{input_image.height}px"
        )

    with info_col3:
        st.metric(
            "File Size",
            f"{uploaded_file.size / (1024 * 1024):.2f} MB"
        )


    st.divider()

    # ORIGINAL IMAGE
    st.subheader("Original Image")

    st.image(
        input_image,
        use_container_width=True
    )

    # REMOVE BUTTON
    if st.button(
        "✨ Remove Background",
        use_container_width=True
    ):

        with st.spinner(
            "AI is removing the background..."
        ):

            try:

                output_image, processing_time = (
                    remove_background(input_image)
                )

            except Exception as error:

                st.error(
                    "Something went wrong while processing "
                    "the image."
                )

                st.exception(error)

                st.stop()

        # BACKGROUND REPLACEMENT
        if background_option == "White":

            background = Image.new(
                "RGBA",
                output_image.size,
                (255, 255, 255, 255)
            )

            output_image = Image.alpha_composite(
                background,
                output_image.convert("RGBA")
            )


        elif background_option == "Black":

            background = Image.new(
                "RGBA",
                output_image.size,
                (0, 0, 0, 255)
            )

            output_image = Image.alpha_composite(
                background,
                output_image.convert("RGBA")
            )

        elif background_option == "Custom Color":

            rgb_color = ImageColor.getrgb(
                custom_color
            )

            background = Image.new(
                "RGBA",
                output_image.size,
                (
                    rgb_color[0],
                    rgb_color[1],
                    rgb_color[2],
                    255
                )
            )

            output_image = Image.alpha_composite(
                background,
                output_image.convert("RGBA")
            )

        # RESULTS
        st.success(
            "Background removed successfully!"
        )


        st.subheader("Result")


        col1, col2 = st.columns(2)


        with col1:

            st.markdown("### Before")

            st.image(
                input_image,
                use_container_width=True
            )


        with col2:

            st.markdown("### After")

            st.image(
                output_image,
                use_container_width=True
            )

        # PROCESSING STATISTICS
        st.subheader("Processing Statistics")

        stat1, stat2, stat3 = st.columns(3)

        with stat1:

            st.metric(
                "Processing Time",
                f"{processing_time:.2f} sec"
            )

        with stat2:

            st.metric(
                "Input Resolution",
                f"{input_image.width} × "
                f"{input_image.height}"
            )

        with stat3:

            st.metric(
                "Output Resolution",
                f"{output_image.width} × "
                f"{output_image.height}"
            )

        # DOWNLOAD
        output_bytes = image_to_bytes(
            output_image
        )


        st.download_button(
            label="⬇️ Download Result",
            data=output_bytes,
            file_name="bgenius_result.png",
            mime="image/png",
            use_container_width=True
        )