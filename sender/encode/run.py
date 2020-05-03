from encoder import encoder

def main():
  '''
  Driver code.

  Parameters:
    None
  
  Return:
    None
  '''
  objEncoder = encoder()
  objEncoder.encodeMessage()
  print("Encoding - Message Encode in Image.    (1/2)")

if __name__ == '__main__':
  main()
