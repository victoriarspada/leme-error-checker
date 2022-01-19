"""
LEME Validation program of XML files.

The program takes the name of an XML file as an input and validates
the XML encoding by calling validate(), which validates the file against
the rules outlined in the XML Schema Definition (XSD) leme.xsd, and outputs
whether or not the file is valid.

Error messages regarding whether or not the XML is well-formed is saved into a file
called 'error_syntax.log', and errors with respect to LEME's encoding rules are
reported in 'error_schema.log'.

Author: Victoria Spada
Contact_ victoria.spada@mail.utoronto.ca
Last Edit: Fri Jan 29 2021.
"""
import os 
from lxml import etree
from validator import *

if __name__ == "__main__":
    while True:
        xml_path = input("What is the name of the file to be validated? ")
        xsd_path = "leme.xsd"  
        print(xml_path[0:len(xml_path)-4])
        valid = validator(xml_path, xsd_path)
        if valid==True:
            print('Validated XML-encoded text. No syntax or encoding errors found.')
        else:
            print('ERROR.')
        next_action = input("Press 'Enter' to exit the application, or type any other key to validate another file.  ")
        if next_action=="":
            break