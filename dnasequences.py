import sys
import numpy as np

class dnasequence:
  """Class dnasequences creates and modifies sequences of DNA bases.
  
  Attributes:
  
  bases: the allowable DNA bases A,C,G,T
  seq: a string of bases without separating punctuation such as "ACGT".
  complements: a dict of complementary bases.
  """

  # "magic" initialisation method
  # seq is optional input, default is "" (empty string)
  def __init__(self,seq=""):
    """__init__ does not usually have a docstring."""

    # Initialise attributes:
    # set bases
    self.bases=np.asarray(["A","C","G","T"])
    # the complements attribute is a dict (dictionary) containing complementary base pairs.
    # Example of usage: self.complements["A"] returns "T".
    self.complements={
      "A": "T",
      "T": "A",
      "C": "G",
      "G": "C"
    }

    # First test: check if input seq is an iterable type
    try:
      it = iter(seq)
    # if not, exit
    except TypeError:

      print(seq, "is not a valid object for creating a sequence. Exiting program.")
      sys.exit()

    # the attribute seq is a numpy array defined from the input string seq
    # define the sequence in different type for easy operation 
    self.seq = np.array(list(seq))
    self.str= str(seq)
    self.list = list(seq)
    
    # Second test: check seq contains only valid bases by calling isdna method
    if(not self.isdna()):
      print("seq contains invalid bases. Exiting program.")
      sys.exit()
    
    return None

  def isdna(self):
    """Check that self.seq only contains valid DNA bases.
    Returns True if so, else False."""
    # Task 1: my code here
    listself = list(self.seq)

    a = listself.count("A")
    b = listself.count("C")
    c = listself.count("G")
    d = listself.count("T")
    n_t = a+b+c+d

    if (len(self.seq) == n_t):
      passes = True
    else: 
      passes = False 
      
    return passes

  
  # example method
  def isequal(self,other):
    """Test if a DNA sequence is identical to this one."""

    # test lengths are equal.
    if(len(self.seq) != len(other.seq)):
      print("Sequences are of different lengths. isequal() returning False.")
      equal=False
    # if equal lengths, test if values are all equal.
    else:
      equal=all(self.seq==other.seq)
    # return True or False
    return equal


  def findcomplement(self):
    """find the complement of a sequence."""
    new_seq = []
    
    for i in self.seq:
      new_seq.append(self.complements[i])

    return new_seq

  
  def firstnonmatch(self,other):
    """find the index of first nonmatch bases"""
    if(len(self.seq) == len(other.seq)):
      i = -1
      j = 0

      while (i < 0):
        if (self.seq[j] != other.seq[j]):
          i = j
        j = j + 1

      return i

    else: 
      print("sorry length of two sequence not equal")
      sys.exit()

  def findgene(self,s_signal):
    """this find the different pieces of gene on a DNA sequence"""
    if (self.isdna() == True):
      # make sure it is dna so we find the pieces of gene

      mygene = []
      stop_signal = s_signal
      dnastring = self.str

      while (dnastring.find(stop_signal) != -1):
        gene_location = dnastring.find(stop_signal)
        
        if (gene_location > 0):
          #if the separator is not at the beginning of the string
          #append and substring from [0:separator]
          mygene.append(dnastring[0:gene_location])
          # append piece of dna to mygene list one by one

          dnastring = dnastring[gene_location+len(stop_signal):]
          #remove the part that is appened to mygene and the separator     

        else:
          
          dnastring = dnastring[gene_location+len(stop_signal):]
          #just remove the separator

      if (len(dnastring) > 0):
        mygene.append(dnastring)
      #append the last piece of gene when no more separato found 
      #then can return the full list of my gene
      #and only append when we have a piece of gene that is not null

      return mygene

    else: 
      print ("not dna cannot find gene")
      sys.exit()


  def firstgene(self, s_signal):
    """this find the first piece of gene on a DNA sequence"""
    firstgene = self.findgene(s_signal)[0]
    return(firstgene)

  def findmutation(self,other,s_signal):
    """this find the number of mutations located on each gene 
       for two DNA sequence of same length."""

    selfgene = self.findgene(s_signal)
    othergene = other.findgene(s_signal)
    mutation = [0]*len(selfgene)


    for i in range(len(selfgene)):
      selfgenei = selfgene[i]
      othergenei = othergene[i]
      for j in range(len(selfgenei)):
        if (selfgenei[j] != othergenei[j]):
          mutation[i] = mutation[i] + 1

    return mutation







    

