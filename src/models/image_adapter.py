import os
import base64
from abc import ABC, abstractmethod
from config.settings import PROFILE

class ImageAdapter(ABC):
    @abstractmethod
    def upload(self, image_name, image_data):
        pass

    @abstractmethod
    def download(self, image_name):
        pass

class ImageLocalAdapter(ImageAdapter):
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def upload(self, image_name, image_data):
        image_path = os.path.join(self.folder_path, image_name)
        with open(image_path, 'wb') as f:
            f.write(base64.b64decode(image_data))
        return image_path

    def download(self, image_name):
        image_path = os.path.join(self.folder_path, image_name)
        if os.path.exists(image_path):
            with open(image_path, 'rb') as f:
                return base64.b64encode(f.read()).decode('utf-8')
        else:
            return None

class ImageDBAdapter(ImageAdapter):
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def upload(self, image_name, image_data):
        # Implemente a lógica para salvar a imagem no banco de dados
        pass

    def download(self, image_name):
        # Implemente a lógica para buscar a imagem no banco de dados
        pass

def get_image_adapter():
    if PROFILE == 'local':
        folder_path = 'static/images'  # Defina o caminho para a pasta local
        return ImageLocalAdapter(folder_path)
    else:
        # Conexão com o banco de dados H2
        db_connection = None  # Suponha que você tenha uma conexão com o banco de dados
        return ImageDBAdapter(db_connection)
