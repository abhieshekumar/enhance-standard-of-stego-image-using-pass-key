import path
from privateImage import privateImage
from keyDecoder import keyDecoder
from keyTemplate import keyTemplate
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

  def driver(self):

    privateImageObj = privateImage()
    image = np.copy(privateImageObj.getPrivateImage())
    height = privateImageObj.getPrivateImageHeight()
    width = privateImageObj.getPrivateImageWidth()

    #Hashed Image
    objWithHash = withHash()
    hashedResult = objWithHash.withHash(height, width, image)

    #Now let's flatten the Hashed Result
    objFlatten = flatten()
    flattenedResult = objFlatten.adjustBars(hashedResult)

    #Converting numpy array to PIL image
    
    flattenedResult = flattenedResult.astype(np.uint8)
    arrayAsPIL = Image.fromarray(flattenedResult, mode='L')

    #Now let's randomize flattened image
    objRandomized = randomize()
    randomizedResult = objRandomized.randomize(arrayAsPIL)

    #The final step xor the above image with key
    objFinal = final()
    result = objFinal.xor(randomizedResult)

    objKeyDecoder = keyDecoder()
    result = objKeyDecoder.decodeKey(result)

    objKeyTemplate = keyTemplate()
    data = objKeyTemplate.getTemplate(result)
    f = open("../metadata/key.py","w")
    f.write(data)
    f.close()