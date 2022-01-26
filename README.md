Author: Victoria Spada  
Contact: victoria.spada@mail.utoronto.ca

# LEME Preprocessing & Validation readME file
-------------------------------------------
The preprocessing and validation programs were created to:  
(1) take a input .txt file and output the same file as an .xml file.  
(2) scan the outputted .xml file from the preprocessing program and 
validate whether the file is encoded according to LEME's encoding rules.    

## Setup
`git clone https://www.github.com/victoriarspada/leme-error-checker`  
`cd leme-error-checker`  
`pip install pyinstaller`  
  
Create the executable for the preprocessing program:  
`pyinstaller --onefile txt_to_xml.py`  
  
Creeate the executable for the validation program:  
`pyinstaller --onefile main.py`  
  
Open the executables in `dist` to run the programs.  

## PREPROCESSING PROGRAM
### txt_to_xml.exe
This program performs the preprocessing steps to fix TXT documents and create well-formed XML.
CREDIT: This code was taken from Tim Alberdingk Thijm's (Princeton University) preprocessor for LEME, and slightly edited by Victoria Spada.  
  
The text file being converted must in the current working directory. 

The name of the file is given as an input (ie, `test/test.txt`), and the XML version of the file is saved in the current
working directory (ie, as `test_prep.xml`).  
  
Associated files: txt_to_xml.py  
  
## VALIDATION PROGRAM
### main.exe
The program takes the name of an XML file as an input and validates
it by calling validate(), which validates the file against the rules
outlined in the XML Schema Definition (XSD) `leme.xsd`. The program prints
a message stating whether or not the file is valid.   
  
Error messages regarding whether or not the XML is well-formed is saved into a file in the `logs` folder,
called `error_syntax.log`, and errors with respect to LEME's encoding rules are
reported in `error_schema.log`.  

Associated files: `main.py, validate.py, leme.xsd`
