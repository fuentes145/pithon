#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 07:13:45 2020

@author: felipe

"""
import unittest.mock
mock = unittest.mock.MagicMock()
mock.side_effect = iter([7,
                           'i 1',
                           'i 2',
                           'i 0',
                           'i 3', 
                           'i 6',
                           'i 5',
                           'd 3'
                           
                 
                           ])

class Node():
    def __init__(self, data, position):
        self.data = data
        self.position = position
        print(self.position)
        self.left = None
        self.right = None
        
    
    def add (self, data):
        if self.data > data:
            if self.left:
                self.left.add(data)
            else:
                self.left = Node(data, self.position*2)
        else:
            if self.right:
                self.right.add(data)
            else:
                self.right = Node(data, self.position*2+1)
        
    
        
        def maximo(self, data):
            if self.right:
                self.right.maximo(data)
            else:
                return self.data
            
        def minimo(self, data):
            if self.left:
                self.minimo(data)
            else:
                return self.data
                
        
        
    def remove (self, data):
        
        if data < self.data:
            if self.left:
                self.left = self.left.remove(data)
        elif data > self.data:
            if self.right:
                self.right = self.right.remove(data)
            
        if data == self.data:
            print(self.position)
            if self.right is None and self.left is None:
                return None
            elif self.right is None:
                return self.left
            elif self.left is None:
                return self.right
            else: 
                
                remplaso = self.left.maximo(data)
                self.data = remplaso
                self.right = self.right.remove_sin_print(remplaso)
                
        return self
    
    def remove_sin_print (self, data):
        
        if data < self.data:
            if self.left:
                self.left = self.left.remove(data)
        elif data > self.data:
            if self.right:
                self.right = self.right.remove(data)
            
        if data == self.data:
            
            if self.right is None and self.left is None:
                return None
            elif self.right is None:
                return self.left
            elif self.left is None:
                return self.right
            else: 
                
                remplaso = self.left.maximo(data)
                self.data = remplaso
                self.right = self.right.remove(remplaso)
                
        return self
            
            

N = int(mock())
data = int(mock().split()[1])
tree = Node(data, 1)
for i in range(1, N):
    info = mock().split()
    if info[0] == "i":
       tree.add(int(info[1])) 
    if info[0] == 'd':
        tree.remove(int(info[1]))