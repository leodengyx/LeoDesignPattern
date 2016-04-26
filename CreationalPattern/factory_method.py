class AbstraceImageReader(object):

    def __init__(self):
        pass

    def getDecodedImage(self):
        raise NotImplementedError("Must implement this function")

class GifImageReader(AbstraceImageReader):

    def __init__(self):
        super(GifImageReader, self).__init__()
        print("New GifImageReader instance created.")

    def getDecodedImage(self):
        print("Get Gif image decoded content")

class JpegImageReader(AbstraceImageReader):

    def __init__(self):
        super(JpegImageReader, self).__init__()
        print("New JpegImageReader instance created.")

    def getDecodedImage(self):
        print("Get Jpeg image decoded content")

if __name__ == "__main__":
    imageReader = GifImageReader()
    imageReader.getDecodedImage()

    imageReader = JpegImageReader()
    imageReader.getDecodedImage()