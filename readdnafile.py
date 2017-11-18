import sys # for exiting on errors
import numpy as np
import random
import matplotlib.pyplot as plt
import dnasequences as dna # import user-defined DNA sequence class

def readfile(myfile):
  """this function readfile datafile
      that has first row with basic information 
      secondrow of DNA sequence
      it will return the  """
  mydata = open(myfile,"r")
  basicinfo = mydata.readline()
  mydna = mydata.readline()
  mydna = dna.dnasequence(seq=mydna)
  return mydna

def main():
  #this is the main function where we do plots and other cool things
  dna1 = readfile("genome_01.dat")
  #we find the length of the DNA in genome_01.dat
  length_1 = len(dna1.seq)

  print("the length of DNA in genome_01.dat is %.0f" %length_1)

  #find the first gene by call firstgene()
  
  sepa = "AAAAAAAAAATTTTTTTTTT"
  dna1_firstgene = dna1.firstgene(sepa)
  #print out the length of firstgene
  print("the length of the first gene in genome_01.dat is %.0f" %len(dna1_firstgene))
  
  #find the list contains all gene by call findgene()
  dna1_allgene = dna1.findgene(sepa)
  dna1_number = len(dna1_allgene)
  dna1_len = [0]*dna1_number
    
  for j in range(len(dna1_allgene)):
    dna1_len[j] = len(dna1_allgene[j])
   
  x = list(range(len(dna1_len)))
  
  #plot bar chart of length of genes in DNA1
  plt.figure(figsize=(10,6))
  plt.bar(x, dna1_len, 1)
  plt.xlabel('Gene index',fontsize=16,color='black')
  plt.ylabel('Gene length', fontsize=16,color='black')
  plt.title('Gene length of genome_01.dat',fontsize=20, color='black')
  
  #delete the #below if you would like to save plot
  plt.savefig('len01.png')
  plt.show()

  
  dna2 = readfile("genome_02.dat")
  #read genome_01.dat and find the mutation 
  mut = dna1.findmutation(dna2,sepa)
  
  #plot scatter chart of mutation vs length of gene
  plt.figure(figsize=(10,6))
  plt.scatter(dna1_len, mut, s=100, marker = '*', color = 'green')
  plt.xlabel('Gene length',fontsize=16,color='black')
  plt.ylabel('number of mutation', fontsize=16,color='black')
  plt.title('mutation vs gene length',fontsize=20, color='black')
  plt.ylim(ymin=0)
  plt.xlim(xmin=0)
  
  #delete the #below if you would like to save plot
  plt.savefig('mutation.png')
  plt.show()
    

  return

main()

