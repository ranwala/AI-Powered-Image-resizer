from image_service import ImageService


def main():
    # Create an instance
    image_service = ImageService()

    # Get all image paths
    image_paths = image_service.get_all_image_paths()

    # Resize all images
    image_service.resize_image(image_paths)


if __name__ == '__main__':
    main()