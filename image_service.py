import glob
import os
import base64
from PIL import Image

from ai_service import AIService

class ImageService:
    def __init__(self):
        self.__base_path = 'images/'
        self.__extensions = ['*.jpg', '*.jpeg', '*.png']
        self.__image_paths = []
        self.__output_dir = 'resized_images'
        self.__ai_service = AIService()


    @classmethod
    def __encode_image(cls, image_path):
        """ Encode image """
        with open(image_path, 'rb') as file:
            return base64.b64encode(file.read()).decode('utf-8')


    def __save_resized_image(self, resized_image, base_name):
        """ Save resized image """
        try:
            output_dir_path = os.path.dirname(self.__output_dir)

            if not output_dir_path:
                os.makedirs(self.__output_dir, exist_ok=True)

            resized_image.save(f"{self.__output_dir}/resized_{base_name}")

        except FileNotFoundError as e:
            print(f"Create out put directory error: {e}")


    def get_all_image_paths(self):
        """ Get all image paths """

        try:
            for ext in self.__extensions:
                self.__image_paths.extend(glob.glob(os.path.join(self.__base_path, ext)))

            return self.__image_paths

        except FileNotFoundError as e:
            print(f"Get all image paths error: {e}")


    def resize_image(self, image_paths):
        """ Resize images """

        print("AI powered image resizing start...")
        try:
            for image_path in image_paths:
                image = Image.open(image_path)
                w, h = image.size

                # Encode to base 64
                encoded_image = self.__encode_image(image_path)

                # Analyse by AI
                ai_response = self.__ai_service.analyse_image(encoded_image)

                if not ai_response:
                    print(f'📸 {os.path.basename(image_path)}')

                    new_size = (int(w * 0.5), int(h * 0.5))

                    print(f'✅ Resized to: {new_size[0]}x{new_size[1]} \n')

                    resized_image = image.resize(new_size)

                    self.__save_resized_image(resized_image, os.path.basename(image_path))

            print("AI powered image resizing finish...")

        except Exception as e:
            print(f"Resize image error: {e}")