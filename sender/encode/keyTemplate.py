class keyTemplate:

  def __init__(self):
    pass
  
  def getTemplate(self, data):
    '''
    Returns a formatted string to be written in key.py

    Parameters:
      data  - a list of exceptions
    
    Returns:
      (str) - a formatted string to be written in key.py
    '''
    string = '''
class key:

  def __init__(self):
    pass

  def getKey(self):   
'''
    data = str(data)
    data = string+"    return "+data+"\n"
    return data
