# aiden Clarke 
#10/15/23
#this progrm is going to calc the answer from deviding from x 

def divisor():
  div = int(input("Enter a number to divide by: "))
  return div

def number_divby():
  dvn = int(input("Enter a number to divide by the divider: "))
  return dvn

def get_awnser(div, dvn):
  if div == 0:
    print("Cannot divide by 0")
    return
  else:
    awnser = dvn / div
    return awnser

def output(div, dvn, awnser):
  print(f"""
  The result of your division operation is:
  |----------------------------------------|
  |   divisor        number to divider     |
  |    {div}             {dvn}                    |
  |                                        |
  |         answer to you problem          |
  |                                        |
  |                {awnser}                     |
  |                                        |
  |----------------------------------------|
  """)

def main():
  div = divisor()
  dvn = number_divby()
  awnser = get_awnser(div, dvn)
  output(div, dvn, awnser)

if __name__ == "__main__":
  main()
