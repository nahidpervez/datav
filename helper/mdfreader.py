#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 22:32:13 2018

@author: mdnahidpervez
"""
import asammdf as mdf
class mdfreader:
    def __init__(self, filename):
        self.filename = filename
        self.mobj = mdf.MDF(filename,'minimum')
        
    def readChannels(self,channels):
        
        
        

