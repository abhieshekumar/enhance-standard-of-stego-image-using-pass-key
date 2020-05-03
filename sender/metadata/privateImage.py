import png
import numpy as np

class privateImage:

  def __init__(self):
    pass
  
  def getPrivateImage(self):
    '''
    Returns the privateImage.png as a 2D numpy array

    Parameters:
      None
    
    Returns:
      (uint8) - A 2D numpy array of privateImage.png
    '''
    
    r = png.Reader(filename = "../asset/privateImage.png")
    row_count, column_count, pngdata, meta = r.asDirect()
    image_2d = np.stack(map(np.uint8, pngdata))
    imageAsArray = np.copy(image_2d)
    return imageAsArray

  def getPrivateImageHeight(self):
    '''
    Returns the height of privateImage.png

    Parameters:
      None
    
    Returns:
      (int) - Height of privateImage.png
    '''

    r = png.Reader(filename = "../asset/privateImage.png")
    row_count, column_count, pngdata, meta = r.asDirect()
    return column_count
  
  def getPrivateImageWidth(self):
    '''
    Returns the width of privateImage.png

    Parameters:
      None
    
    Returns:
      (int) - Width of privateImage.png
    '''
    r = png.Reader(filename = "../asset/privateImage.png")
    row_count, column_count, pngdata, meta = r.asDirect()
    return row_count
  
  def getPrivateImageLevels(self):
    '''
    Returns the possible values that can take a pixel value in the private image

    Parameters:
      None
    
    Returns:
      (int) - pixel values that can be used
    '''
    return 256

  def getTolerance(self):
    '''
    Returns the tolerance value used in flat.py

    Parameters:
      None
    
    Returns:
      (double) - returns the tolerance value
    '''
    return 0.5
