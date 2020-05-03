import path
import numpy as np
import png
from key import key
import math

class decoder:
  def __init__(self):
    pass

  def decode(self):

    '''
    Prints the decoded message.

    Parameter:
      None
    
    Returns:
      None.
    '''
    
    r = png.Reader(filename = "../received/stegoImage.png")
    height, width, pngdata, meta = r.asDirect()
    image_2d = np.stack(map(np.uint8, pngdata))
    imageAsArray = np.copy(image_2d)
    
    objKey = key()
    exceptionKey = objKey.getKey()

    wrd, dM = '', ''
    COUNT = 8
    arr, startPos = 0, 0

    isException = False
    i = 0

    while i < height*width:
      px = i%width
      py = math.floor(i/width)
      if len(exceptionKey) == 0:
        pass
      elif (px, py) in exceptionKey:
        isException = True
        index = exceptionKey.index((px, py))
        del exceptionKey[index]

      currPixel = imageAsArray[px][py]
      currPixelBin = "{0:b}".format(currPixel)
      while len(currPixelBin) < 8:
        currPixelBin='0'+currPixelBin
      
      currPixelBin = "".join(reversed(currPixelBin))

      try:
        indexOfZero = currPixelBin.index( '00' )
      except:
        indexOfZero = -1
      
      try:
        indexOfOne = currPixelBin.index( '11' )
      except:
        indexOfOne = -1

      if indexOfZero == -1 and indexOfOne == -1:
        ans = currPixelBin[0]
      elif indexOfZero == -1 and indexOfOne>=0:
        ans = 1
      elif indexOfZero >= 0 and indexOfOne==-1:
        ans = 0
      elif indexOfZero < indexOfOne:
        ans = 0
      elif indexOfZero > indexOfOne:
        ans = 1
      

      if isException:
        if ans==0:
          ans=1
        elif ans==1:
          ans=0
      #00001001
      isException = False

      wrd = wrd+''+str(ans)
      COUNT -= 1
      if COUNT == 0:
        wrd = int(wrd, 2)
        wrd = str(chr(wrd))
        if wrd == "\x00":
          break
        dM += wrd
        wrd = ''
        COUNT = 8      
      i += 1
    
    print("Decoding - Message Decoded.            (2/2)")
    print("Result   - Decoded Message - "+dM)
