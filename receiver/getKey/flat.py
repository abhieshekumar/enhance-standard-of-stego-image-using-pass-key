import numpy as np

class flatten:

  def __init__ (self):
    pass
  
  def adjustBars(self, matrix):
    '''
    Flattens the frequency of values in matrix

    Parameters:
      matrix  - A numpy matix
    
    Returns:
      (uint8) - A 2D matrix with values flattened according to tolerance
    '''
    return matrix
    levels = 256
    rows, cols = matrix.shape
    matrix = matrix.flatten()
    
    freq = np.empty([levels])
    threshold = (rows*cols)//levels

    tolerance = 0.5

    for i in range(levels):
      freq[i] = np.sum(matrix == i)

    while True:

      toAdjust = freq - threshold
      toAdjust = toAdjust != 0
      toAdjust = np.sum(toAdjust)
      toAdjustFract = toAdjust/levels
      if toAdjustFract <= tolerance:
        break

      #index of maximum and minimum element
      temp = np.copy(freq)
      temp[temp == threshold] = np.nan

      tallestInd = np.nanargmax(temp)
      shortestInd = np.nanargmin(temp)

      if temp[shortestInd] >= threshold:
        print("The shortest bar is "+str(temp[shortestInd])+" and threshold is "+str(threshold))
        break
      elif temp[tallestInd] <= threshold:
        print("The tallest bar is "+str(temp[tallestInd])+" and threshold is "+str(threshold))
        break
      else:
        #there is hope of filling in
        heightToFill = int(threshold - temp[shortestInd])
        availableHeight = int(temp[tallestInd] - threshold)

        #index of occurance of tallest
        candidateLocations = np.where(matrix == tallestInd)[0]
        candidateLocations = candidateLocations[:availableHeight]

        if availableHeight >= heightToFill:
          matrix[candidateLocations[:heightToFill]] = shortestInd
          freq[shortestInd] = freq[shortestInd] + heightToFill
          freq[tallestInd] = freq[tallestInd] - heightToFill
        else:
          matrix[candidateLocations] = shortestInd
          freq[shortestInd] = freq[shortestInd] + len(candidateLocations)
          freq[tallestInd] = freq[tallestInd] - len(candidateLocations)
    
    matrix = matrix.reshape((rows, cols))
    matrix = matix.astype(np.uint8)
    return matrix