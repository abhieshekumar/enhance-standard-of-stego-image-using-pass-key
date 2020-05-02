import numpy as np
import png

class final:

  def __init__(self):
    pass
  
  def xor(self, image):
    '''
    Returns the final XORed image with the key.

    Parameters:
      image - Image to perform XOR with
    
    Returns:
      (uint8) - 2d representation of key
    '''
    r = png.Reader(filename = "../received/key.png")
    row_count, column_count, pngdata, meta = r.asDirect()
    image_2d = np.stack(map(np.uint16, pngdata))
    keyImage = np.copy(image_2d)
    
    image = image.astype(np.uint8)

    result = np.bitwise_xor(image, keyImage)
    return result
