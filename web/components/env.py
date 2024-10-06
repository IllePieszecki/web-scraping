import os
from dotenv import load_dotenv


class Config:
    @staticmethod
    def load_environment_variables():
        load_dotenv()

    @staticmethod
    def get_image_path():
        return os.getenv("IMAGE_PATH")
