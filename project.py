import sys # for exiting on errors
import numpy as np
import random
import matplotlib.pyplot as plt
import dnasequences as dna # import user-defined DNA sequence class

def randomstr(N):
  """Generate a random string of bases of length N"""
  return "".join([random.choice('ACGT') for i in range(N)])


def main():

  # generate a random string of bases of length 10.
  # this is a single-stranded DNA sequence.
  #mystr=randomstr(10)
  #print(mystr)
  # example DNA sequence strings for testing
  crick_str= "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"
  # this is the complement of crick_str
  watson_str="TACCGGTAACATTACCCGGCGACTTTCCCACGGGCTATC"
  # crick with insert mutations
  crick2_str= "ATGGCCATTGTAATGGGCCGCTGAAACGGGTGCCTCGATAG"

  
  # TEST: make a dnasequence instance with an empty sequence.
  #myseq=dna.dnasequence()
  # this is how to print the seq attribute of a dnasequence
  #print(myseq.seq)
  
  # TEST: make a dnasequence instance with an invalid sequence.
  # should return a fatal error.
  #myseq=dna.dnasequence(seq="U")
  
  # this is how to create a dnasequence instance from mystr.
  #myseq=dna.dnasequence(seq=mystr)
  #print(myseq.seq)
  
  # My code starts here...
  
  ####task 2, call our findcomplement method
  #and check if watson_compliment is same as crick and the result will be printed 
  watson = dna.dnasequence(seq=watson_str)
  crick = dna.dnasequence(seq=crick_str)
  watson_compliment = watson.findcomplement()
  watson_compliment = dna.dnasequence(seq=watson_compliment)
  check_result = watson_compliment.isequal(crick)
  print('the compliment of watson_str is same as crick_str: %s' %check_result)
  
  ####task 3, find the fist non match of two DNA sequence 
  crick2 = dna.dnasequence(seq=crick2_str)

  crick_nonmatch = crick.firstnonmatch(crick2)

  print ('the index of first non matching of crick_str and crick2_str is: %.0f' %crick_nonmatch)
  
  
  return

main()

