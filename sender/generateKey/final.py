from keyEncoder import keyEncoder
import numpy as np

class final:

  def __init__(self):
    pass
  
  def xor(self, image):
    '''
    Returns the final XORed image with the key.

    Parameters:
      image - Image to perform XOR with
    
    Returns:
      (uint8) - XORed 2D representation of final result
    '''
    objKeyEncoder = keyEncoder()
    keyMatrix = objKeyEncoder.keyToMatrix()

    result = np.bitwise_xor(image, keyMatrix)
    result = result.astype(np.uint8)
    return result
