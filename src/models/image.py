from iomg_data_keeper.src.models.image_adapter import get_image_adapter

class Image:
    def __init__(self):
        self.adapter = get_image_adapter()

    def upload_image(self, image_name, image_data):
        return self.adapter.upload(image_name, image_data)

    def download_image(self, image_name):
        return self.adapter.download(image_name)
