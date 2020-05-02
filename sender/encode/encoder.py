import numpy as np
import png
import math
import path
from message import message
from privateImage import privateImage
from keyTemplate import keyTemplate

class encoder:

  def __init__(self):
    pass
  
  def encodeMessage(self):
    '''
    Encodes the message from ../message.py to ../privateImage.py and generates the stegoImage along with the relevant key.

    Parameters:
      None
    
    Returns:
      (stegoImage.png) - stego.png stored in ../output/stegoImage.png
      (key.py)         - a key of exceptions. It is also stored in ../output/key.py
    '''

    privateImageObj = privateImage()
    image = np.copy(privateImageObj.getPrivateImage())
    height = privateImageObj.getPrivateImageHeight()
    width = privateImageObj.getPrivateImageWidth()

    objMessage = message()
    msg = objMessage.getMessage()
    msgLen = objMessage.getMessageLength()

    objKeyTemplate = keyTemplate()

    startIndex = 0
    pvtkey = []

    for i in range(msgLen):
      
        currChar = msg[i]
        currCharBin = "{0:b}".format(ord(currChar))
        while len(currCharBin) < 8 :
          currCharBin='0' + currCharBin

        for j in range(8):
          currBit = currCharBin[j]
          currPixel = image[startIndex%width][math.floor(startIndex/width)]
          currPixelBin = "{0:b}".format(currPixel)
          while len(currPixelBin) <8 :
            currPixelBin ='0' + currPixelBin          
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
            ans = -1
          elif indexOfZero == -1 and indexOfOne >= 0:
            ans = 1
          elif indexOfZero >= 0 and indexOfOne == -1:
            ans = 0
          elif indexOfZero < indexOfOne:
            ans = 0
          elif indexOfZero > indexOfOne:
            ans = 1          
          newPixelBin=currPixelBin
          if ans==0 and currBit=='1':
            pvtkey.append(tuple([startIndex%width, math.floor(startIndex/width)]))
          elif ans==1 and currBit=='0':
            pvtkey.append(tuple([startIndex%width, math.floor(startIndex/width)]))
          elif ans == -1:
            newPixelBin = currBit+newPixelBin[1:]          
          newPixelBin = "".join(reversed(newPixelBin))
          newPixel = str(int(newPixelBin, 2))
          image[startIndex%width][math.floor(startIndex/width)] = newPixel
          startIndex += 1

    image = image.astype(np.uint8)
    png.from_array(image, mode="L").save("../../receiver/received/stegoImage.png")
    
    data = objKeyTemplate.getTemplate(pvtkey)
    f = open("../metadata/key.py","w")
    f.write(data)
    f.close()