from driver import driver
import sys

def main():
  '''
  Driver code.

  Parameters:
    None
  
  Return:
    None
  '''

  objDriver = driver()
  
  if len(sys.argv) == 1:
    objDriver.driver(None)
  else:
    objDriver.driver(decorator = sys.argv[1])

if __name__ == '__main__':
  main()