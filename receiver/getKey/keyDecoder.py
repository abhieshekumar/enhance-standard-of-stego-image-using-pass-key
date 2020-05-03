import numpy as np
class keyDecoder:

  def __init__(self):
    pass
  
  def decodeKey(self, matrix):
    '''
    Converts 2D array representation to list.

    Parameters:
      matrix - A 2D matrix corresponding to key.

    Returns:
      (list) - A list with indexes to key.
    '''
    return list(zip(*np.where(matrix == 1)))
