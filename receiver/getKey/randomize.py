import path
import numpy as np
from PIL import Image
from private import private
import random

class randomize:

  def __init__(self):
    self.nshuffle = 1
    self.granularity = 1
  
  def setSeed(self):
    '''
    Sets the seed for Python's random function

    Parameters:
      None

    Returns:
      None
    '''
    objPrivate = private()
    passValue = 0
    password = objPrivate.getSeed()
    for ch in password:                 
        passValue = passValue+ord(ch)
    random.seed(passValue)

  def scrambleBlocks(self, im):
    '''
    Shuffles the input image (im)

    Parameters:
      im - The PIL representation of image to scramble

    Returns:
      (PIL) - a representation of scrambled image
    '''
    self.setSeed()
    width = im.size[0]
    height = im.size[1]
    blockWidth = self.findBlockDim(width)
    blockHeight = self.findBlockDim(height)    
    gridWidthDim = width//blockWidth
    gridHeightDim = height//blockHeight
    nblocks = gridWidthDim*gridHeightDim
    blocks = []
    for n in range(nblocks):
        blocks += [self.getBlock(im,n,blockWidth,blockHeight)]
    newOrder = list(range(nblocks))
    for n in range(self.nshuffle):
        random.shuffle(newOrder)
    newImage = im.copy()
    for n in range(nblocks):
        i = (n%gridWidthDim)*blockWidth
        j = (n//gridWidthDim)*blockHeight
        box = (i,j,i+blockWidth,j+blockHeight)    
        newImage.paste(blocks[newOrder[n]],box)
    return newImage

  def findBlockDim(self, length):
    '''
    Returns the size of block

    Parameters:
      length - the size of block

    Returns:
      (int) - the block size to operate upon
    '''
    candidate = np.arange(self.granularity, length+1)
    answers = candidate[length%candidate == 0]
    answer = np.amin(answers)
    return answer

  def getBlock(self, im, n, blockWidth, blockHeight):
    '''
    Returns the block of im to work upon.

    Parameters:
      im          - the image to work with
      n           - the block number
      blockWidth  - width of the block
      blockHeight - height of the block

    Returns:
      - A cropped section of image
    '''
    width = im.size[0]
    gridWidthDim = width//blockWidth
    i = (n%gridWidthDim)*blockWidth                        
    j = (n//gridWidthDim)*blockHeight
    box = (i,j,i+blockWidth,j+blockHeight)
    blockIm = im.crop(box)      
    return blockIm

  def randomize(self, image):
    '''
    Shuffles the blocks of the input image (im)

    Parameters:
      im - The PIL representation of final output from flat.py

    Returns:
      (uint8) - 2D numpy representation of scrammble image
    '''
    newImage = self.scrambleBlocks(image)
    randomizedPrivateImage = np.asarray(newImage)
    randomizedPrivateImage = randomizedPrivateImage.astype(np.uint8)
    return randomizedPrivateImage
