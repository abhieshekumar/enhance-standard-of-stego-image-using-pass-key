import path
from privateImage import privateImage
import png
from PIL import Image
import numpy as np
from withHash import withHash
from flat import flatten
from randomize import randomize
from final import final

#hash-flat-random-final
class driver:

  def __init__(self):
    pass

  def driver(self, decorator = None):
    '''
    Executes the other scripts in the folder in a specific order to return the key.

    Parameters:
      decorator : It specifies whether to plot histogram and show images during execution.
    
    Returns:
      None. But it writes the key in key.py
    '''

    if decorator:
      from matplotlib import pyplot as plt

    if decorator == 'histogram':
      fig, axs = plt.subplots(5, num="Histogram for Sender")
      binSize = [x for x in range(256)]
    
    if decorator == 'image':
      fig, axs = plt.subplots(2,2, num="Images for Sender")

    privateImageObj = privateImage()
    image = np.copy(privateImageObj.getPrivateImage())
    height = privateImageObj.getPrivateImageHeight()
    width = privateImageObj.getPrivateImageWidth()
    if decorator == 'histogram':
      temp = image.flatten()
      axs[0].hist(temp, bins = binSize)
      axs[0].title.set_text("Original Image")
    
    #Hashed Image
    objWithHash = withHash()
    hashedResult = objWithHash.withHash(height, width, image)
    if decorator == 'histogram':
      temp = hashedResult.flatten()
      axs[1].hist(temp , bins = binSize)
      axs[1].title.set_text("Hashed Image")
    
    if decorator == 'image':
      axs[0][0].imshow(hashedResult, cmap='gray', interpolation='none')
      axs[0][0].title.set_text("Hashed Image")

    #Now let's flatten the Hashed Result
    objFlatten = flatten()
    flattenedResult = objFlatten.adjustBars(hashedResult)
    if decorator == 'histogram':
      temp = flattenedResult.flatten()
      axs[2].hist(temp , bins = binSize)
      axs[2].title.set_text("Flattened Image")
    if decorator == 'image':
      axs[0][1].imshow(flattenedResult, cmap='gray', interpolation='none')
      axs[0][1].title.set_text("Flattened Image")

    #Converting numpy array to PIL image    
    flattenedResult = flattenedResult.astype(np.uint8)
    arrayAsPIL = Image.fromarray(flattenedResult, mode='L')

    #Now let's randomize flattened image
    objRandomized = randomize()
    randomizedResult = objRandomized.randomize(arrayAsPIL)
    if decorator == 'histogram':
      temp = randomizedResult.flatten()
      axs[3].hist(temp , bins = binSize)
      axs[3].title.set_text("Randomized Image")
    if decorator == 'image':
      axs[1][0].imshow(randomizedResult, cmap='gray', interpolation='none')
      axs[1][0].title.set_text("Randomized Image")

    #The final step xor the above image with key
    objFinal = final()
    result = objFinal.xor(randomizedResult)
    if decorator == 'histogram':
      temp = result.flatten()
      axs[4].hist(temp , bins = binSize)
      axs[4].title.set_text("Final Image")
    if decorator == 'image':
      axs[1][1].imshow(result, cmap='gray', interpolation='none')
      axs[1][1].title.set_text("Final Image")

    result = result.astype(np.uint8)
    png.from_array(result, mode="L").save("../../receiver/received/key.png")

    if decorator:
      plt.show()
