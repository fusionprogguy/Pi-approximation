# The formula,
# \pi = \sum_{k=0}^\infty \frac{1}{16^k} \left( \frac{4}{8k + 1} - \frac{2}{8k + 4} - \frac{1}{8k + 5} - #\frac{1}{8k + 6}\right),
# is remarkable because it allows extracting any individual hexadecimal or binary digit of pi without calculating all the preceding ones.
#
# http://www.analyticbridge.com/profiles/blogs/new-state-of-the-art-random-number-generator-simple-strong-and-fa

# import improved precision
#import Decimal

# set decimal precision
#getcontext().prec = 28

# for comparison
import math

def fast_pi(k):
  #approximates pi using a sum formula which takes k as the number of iterations to produce the sum
  fast_pi = 0
  for i in range(k):
    digit = 1/16**i * ( 4/(8*i + 1) - 2/(8*i + 4) - 1/(8*i + 5) - 1/(8*i + 6) )
    fast_pi = fast_pi + digit
    print ("digit =", digit)
  return fast_pi

def main():
  #prints out the approximation for pi given user input for k compared to pi as stored in the math package
  print ("")
  print ("Pi approximation function")
  print ("pi = Sum{i=0 to k} { 1/16**i * ( 4/(8i + 1) - 2/(8i + 4) - 1/(8i + 5) - 1/(8i + 6) ) }")
  print ("")
  n = int(eval(input("Enter Integer to calculate pi with the above formula for k=")))
  pi_approx = fast_pi(n)
  print ("")
  print ("   fast_pi =", pi_approx)
  print ("        pi =", math.pi)
  print ("difference =", math.pi-pi_approx)
  print ("")
  # increased accuracy
  #print ("difference =", Decimal(math.pi) - Decimal(pi_approx))

if __name__ == "__main__":
   main()
