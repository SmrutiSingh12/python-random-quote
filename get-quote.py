import random
def main():
  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = 13
  rnd = random.randint(0, last)
  last = len(quotes) - 1
  #print(quotes)
  #print(quotes[0])
  #print(quotes[-1])
  print(quotes[rnd])

if __name__== "__main__":
  main()
