#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 10:55:22 2019

@author: xhasam
"""
import sys

inputfile= open(sys.argv[1], 'r')

pdbids=[]

for line in inputfile:
    line=line.strip()
    if line.startswith("<num>"):
        numb=int(''.join(element for element in line if element.isdigit()))
    if line.startswith("<id>"):
        pdbnames=line.split("|")[3]
        if pdbnames not in pdbids:
            pdbids.append(pdbnames)
print "Number of PDB ids listed", len(pdbids)

with open('list_pdbids.txt', 'w') as the_file:
    the_file.write( ' '.join(pdbids))
the_file.close()
