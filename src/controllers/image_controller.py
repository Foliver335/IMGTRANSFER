from img_data_keeper.src.models.image import Image
from img_data_keeper.src.views.image_view import ImageView

class ImageController:
    @staticmethod
    def upload_image(image_name, image_data):
        image = Image()
        result = image.upload_image(image_name, image_data)
        if result:
            ImageView.display_success(result)
        else:
            ImageView.display_error("Falha ao fazer upload da imagem.")

    @staticmethod
    def download_image(image_name):
        image = Image()
        result = image.download_image(image_name)
        if result:
            ImageView.display_success("Imagem baixada com sucesso!")
        else:
            ImageView.display_error("Imagem não encontrada.")
