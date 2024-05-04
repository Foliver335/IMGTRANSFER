from flask import Flask, request
from img_data_keeper.controllers.image_controller import ImageController

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    image_name = request.form['image_name']
    image_data = request.files['image_data'].read()
    ImageController.upload_image(image_name, image_data)
    return 'Upload realizado com sucesso!'

@app.route('/download/<image_name>', methods=['GET'])
def download(image_name):
    ImageController.download_image(image_name)
    # Implemente a lógica para retornar a imagem ao usuário
    return f'Imagem {image_name} baixada com sucesso!'

if __name__ == "__main__":
    app.run(debug=True)

