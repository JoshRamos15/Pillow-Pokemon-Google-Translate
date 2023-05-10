from PIL import Image, ImageFilter

def apply_filter(input_image_path, output_image_path):
    # Open the image
    image = Image.open(input_image_path)

    # Apply a filter (e.g., BLUR) to the image
    filtered_image = image.filter(ImageFilter.BLUR)

    # Save the filtered image
    filtered_image.save(output_image_path)

def main():
    # Get the input image path from the user
    input_image_path = input("Enter the path to the input image: ")

    # Get the desired output image path from the user
    output_image_path = input("Enter the path for the output image: ")

    # Apply filter and save the output image
    apply_filter(input_image_path, output_image_path)
    print(f"Filtered image saved to: {output_image_path}")

if __name__ == "__main__":
    main()
