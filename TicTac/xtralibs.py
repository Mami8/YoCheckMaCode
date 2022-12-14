from PIL import Image

def convert_image_to_ico(image, save_dir):
    logo = Image.open(save_dir)
    logo.save(save_dir, format='ICO')

