import path
from private import private
import numpy as np
import hashlib

class withHash:

  def __init__ (self):
    pass

  def getHash(self):
    '''
    Returns a sha56 value of the secret between sender and receiver

    Parameters:
      None
    
    Returns:
      (str) - A sha256 hash of the secret
    '''
    objPrivate = private()
    password = objPrivate.getSeed()
    hashedPassword = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return hashedPassword
  
  def withHash(self, height, width, image):
    '''
    Returns the 'image' cyclically hashed with the output of getHash()

    Parameters:
      height - height of image
      width  - width of image
      image  - a numpy representation of the privateImage

    Returns:
      (uint8) - A 2D numpy array
    '''

    length = height*width
    hash = self.getHash()
    res = (hash * (int(length//len(hash))+1))[:length]
    resAscii = [ord(c) for c in res]
    toNpArray = np.asarray(resAscii).reshape(height, width)
    randomizedPrivateImage = image
    result = np.bitwise_xor(randomizedPrivateImage, toNpArray)
    result = result.astype(np.uint8)
    return result
