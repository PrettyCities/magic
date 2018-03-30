import pytesseract


class ImageReader:
    @classmethod
    def read(cls, image):
        return pytesseract.image_to_string(image=image)
