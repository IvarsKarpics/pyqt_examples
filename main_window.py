#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
import sys
from PyQt4.QtGui import *
 
a = QApplication(sys.argv)       
 
w = QWidget()
w.resize(640, 480)

w.setWindowTitle("Main window") 
w.show() 
 
sys.exit(a.exec_())
