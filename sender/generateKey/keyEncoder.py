import path
from key import key
from privateImage import privateImage
import numpy as np

class keyEncoder:
  def __init__ (self):
    pass
  
  def getKey(self):
    '''
    Returns the array representation of the generated key

    Parameters:
      None

    Returns:
      (list) - a list comprising of key exceptions
    '''
    objKey = key()
    return objKey.getKey()

  def keyToMatrix(self):
    '''
    Convert the getKey() result to a 2D array

    Parameters:
      None

    Returns:
      (int64) - A 2D representation of the getKey(). It is a sparse matrix.
    '''
    privateImageObj = privateImage()
    height = privateImageObj.getPrivateImageHeight()
    width = privateImageObj.getPrivateImageWidth()

    passKey = self.getKey()

    matrixPassKey = np.zeros((height, width))
    for val in passKey:
      matrixPassKey[val[0]][val[1]] = 1
    matrixPassKey = matrixPassKey.astype('int64')

    return matrixPassKey
