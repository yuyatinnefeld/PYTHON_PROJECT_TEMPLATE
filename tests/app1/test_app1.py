#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
---------------------------------------------
# PYTHON TEMPLATE
# (C) 2021 Yuya Tinnefeld, Düsseldorf, Germany
# email: yuyatinnefeld@gmail.com
---------------------------------------------
"""
import unittest
import sys 
import os

cwd = os.getcwd()
tests = os.path.dirname(cwd)
project_path = os.path.dirname(tests)
project_app1 = os.path.join(project_path, "project/app1")
sys.path.insert(1, project_app1)

from app1 import app1Object

class TestMyApp(unittest.TestCase):
    
    def setUp(self):
        print("⚡ setUp ⚡")
        self.emp_1 = app1Object('Otomo', 'Tanaka')
        self.emp_2 = app1Object('John', 'Sherk')
    

    def tearDown(self):
        print("⚡ tearDown ⚡")
        print("---------------------")


    def test_fullname(self):
        print("⚡ test_fullname ⚡")
        self.assertEqual(self.emp_1.fullname, 'Otomo Tanaka')
        self.assertEqual(self.emp_2.fullname, 'John Sherk')

        self.emp_1.first = 'Thomas'
        self.emp_2.first = 'Takashi'
       
        self.assertEqual(self.emp_1.fullname, 'Thomas Tanaka')
        self.assertEqual(self.emp_2.fullname, 'Takashi Sherk')


    def test_email(self):
        print("⚡ test_email ⚡")

        self.assertEqual(self.emp_1.email, 'otomo.tanaka@email.com')
        self.assertEqual(self.emp_2.email, 'john.sherk@email.com')

        self.emp_1.first = 'Thomas'
        self.emp_2.first = 'Takashi'
       
        self.assertEqual(self.emp_1.email, 'thomas.tanaka@email.com')
        self.assertEqual(self.emp_2.email, 'takashi.sherk@email.com')


if __name__ == '__main__':
    print("🐍 run  test_app1.py 🐍")
    unittest.main()