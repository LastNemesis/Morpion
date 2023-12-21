## Import main library
import unittest
import tkinter as tk

## Import the app
from app import main

## Main test-function
class TestApp(unittest.TestCase):
    """ Main test function """

    def setUp(self):
        """ Setting up the test function"""
        

## Call the main function to start the test-application
if __name__ == "__main__":
    unittest.main()