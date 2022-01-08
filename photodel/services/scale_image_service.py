from PIL import Image


def is_vertical_image(img_width, img_height):
    """
    Проверка вертикальная ли картинка
    если да то возвращается True иначе False
    """
    if img_width < img_height:
        return True
    return False


def generate_ratio_for_image(img_width, img_height, crop_width, crop_height):
    """
    Создание коэффициента для пропорционального увеличения одной из сторон
    Если vertical True то картинка вертикальная и используется первое условие иначе второе
    """
    if is_vertical_image(img_width, img_height):
        return (crop_height / img_height) * img_width
    else:
        return (crop_width / img_width) * img_height


def generate_resize_image(open_image, crop_width, crop_height, resize_side):
    """
    Создание перемастштабируемой фото. Если фото больше crop_width, crop_height, то идет
    уменьшение фотки. Если crop_width, crop_height больше чем размер фотки,
    фотка увеличивается до размеров crop_width, crop_height
    Также если ширина картинки меньше высоты то картинка вертикальная и он а масштабируется по ширине, а высоты
    подгоняется по высчтанному коэффцциенту из generate_ratio_for_image функции. Если фото гооризонтальная, то
    она подгоняется по высоте и высчитывается ширина по коэффиенту
    """
    img_width, img_height = open_image.size
    if img_width <= crop_width and img_height <= crop_height:
        return open_image
    if is_vertical_image(img_width, img_height):
        return open_image.resize((int(resize_side), int(crop_height)))
    else:
        return open_image.resize((int(crop_width), int(resize_side)))


def scale_image(photo):
    """
    Масштабирование изображения
    """
    start_image = Image.open(photo)
    crop_width, crop_height = 1200, 1200
    img_width, img_height = start_image.size
    resize_side = generate_ratio_for_image(img_width, img_height, crop_width, crop_height)
    end_img = generate_resize_image(start_image, crop_width, crop_height, resize_side)
    end_img.save('media/' + photo.name)
    return photo.name
