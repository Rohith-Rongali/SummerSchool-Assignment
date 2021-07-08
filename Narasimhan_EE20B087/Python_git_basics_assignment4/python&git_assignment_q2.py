# -*- coding: utf-8 -*-
"""python&git_assignment_q2.ipynb

Automatically generated by Colaboratory.

link for google colab document - https://colab.research.google.com/drive/1_KQTPomUmKOObzqSnr753P7Bb9cVSmBy?usp=sharing
"""

"""
Problem definition: Python class to find a pair of elements (indices of the two numbers) from 
a given array whose sum equals a specific target number.
(*)In this problem I am assuming that the indices cannot be the same. They have to be unique indices. 
example: for target 20 in the list [10,20,30], [0,0] cannot be a solution according to my program.

"""
class Target_Num:
  # class variables
  solutions = {}

  def fun(self, list1, target):
    # instance variables list1, target and solutions

    self.target = target
    self.list1 = list1
    sno = 1
    for i in range(0,len(list1)):                      # searching for pair of indices that add up to the target
      for j in range(0,len(list1)):
        if ((self.target == self.list1[i]+self.list1[j]) and i != j):           # (*)        
          self.solutions[sno] = [i,j]                  # updating solutions dictionary
          sno = sno + 1
    print(self.solutions)
    if (sno == 1 and solutions == {}):                 # no solutions case
      print("No two indices add up to given target")
     
test = Target_Num()
test.fun([10,20,10,40,50,60,70],50)
