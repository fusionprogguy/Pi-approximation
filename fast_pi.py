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

def chud_pi(k):
  #The Chudnovsky brothers found in 1987 that
  #\frac{426880 \sqrt{10005}}{\pi} = \sum_{k=0}^\infty \frac{(6k)! (13591409 + 545140134k)}{(3k)!(k!)^3 (-640320)^{3k}}\!
  #which delivers 14 digits per term.
  chud_pi = 0
  for i in range(k):
    numerator = math.factorial(6*i)*(13591409 + 545140134*i)
    denominator = math.factorial(3*i)*(math.factorial(i))**3*(-640320)**(3*i)
    term = numerator / denominator
    chud_pi = chud_pi + term
    print ("term =", term)
  return chud_pi

def main():
  #prints out the approximation for pi given user input for k compared to pi as stored in the math package
  print ("")
  print ("Pi approximation function")
  print ("pi = Sum{i=0 to k} { 1/16**i * ( 4/(8i + 1) - 2/(8i + 4) - 1/(8i + 5) - 1/(8i + 6) ) }")
  print ("")
  print ("Chudnovsky function")
  print ("426880*sqrt(10005)/pi = Sum{i=0 to k}( (6*i)!*(13591409 + 545140134*i) ) / ( (3*i)!*(i!)**3*(-640320)**(3*i) )")
  print ("")
  # Python 2.x 
  # n = int(eval(raw_input("Enter Integer to calculate pi with the above formula for k=")))
  # Python 3.x 
  n = int(eval(input("Enter Integer to calculate pi with the above formula for k=")))
  pi_approx = fast_pi(n)
  pi_chud = (426880*math.sqrt(10005))/chud_pi(n)
  print ("")
  print ("   fast_pi =", pi_approx)
  print ("   chud_pi =", pi_chud)
  print ("        pi =", math.pi)
  print ("fast difference =", math.pi-pi_approx)
  print ("chud difference =", math.pi-pi_chud)
  print ("")
  # increased accuracy
  #print ("difference =", Decimal(math.pi) - Decimal(pi_approx))

if __name__ == "__main__":
   main()
