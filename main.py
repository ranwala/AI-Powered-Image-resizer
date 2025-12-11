from image_service import ImageService


def main():
    # Create an instance
    image_service = ImageService()

    try:

        # Get all image paths
        image_paths = image_service.get_all_image_paths()

        if image_paths:
            # Resize all images
            image_service.resize_image(image_paths)
        else:
            print("No images found")

    except PermissionError as pe:
        print(f"No permission to write to output directory: {pe}")
    except FileNotFoundError as fe:
        print(f"Directory path is invalid: {fe}")
    except ValueError as ve:
        print(f"Invalid value: {ve}")
    except OSError as oe:
        print(f"File system error while saving images: {oe}")
    except Exception as e:
        print(f'Unknown error: {e}')


if __name__ == '__main__':
    main()