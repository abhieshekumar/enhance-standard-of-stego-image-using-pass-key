class message:
  
  def __init__(self):
    pass
  
  def getMessage(self):
    '''
    Returns the message which has to be embedded

    Parameters:
      None
    
    Returns:
      (str) The message which has to be embedded
    '''
    return "StayHomeStaySafe"
  
  def getMessageLength(self):
    '''
    Returns the length of getMessage()

    Parameters:
      None
    
    Returns:
      (int) The length of getMessage()
    '''
    return len(self.getMessage())
  
  def getMessageSize(self):
    '''
    Returns the size taken by getMessage() in bits

    Parameters:
      None
    
    Returns:
      (int) The size of message in bits.
    '''
    return self.getMessageLength()*8
  