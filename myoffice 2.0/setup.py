#!/usr/bin/python
#coding: utf-8
from distutils.core import setup
import py2exe
import os,sys
home = os.path.dirname(os.path.abspath(sys.argv[0]))
imagedir = os.path.join(home, "images")

setup(
    windows = [
    {
        "script": "runwin.py",
        "icon_resources": [(1, os.path.join(imagedir,"1381love.ico"))]
    }
    ],
)
      
#setup(console=["myoffice.py"])