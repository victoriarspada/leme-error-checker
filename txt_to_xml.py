#!/bin/python
"""
Basic preprocessing steps to fix LEME TXT documents and create well-formed XML.
CREDIT: This code was taken from XXXX and very slightly edited by Victoria Spada.

Contact_ victoria.spada@mail.utoronto.ca
Last Edit: Sat Jan 30 2021.
"""

import re
import sys

def create_pbs(data):
    """
    Change all page tags in data to pb tags.
    pb tags have all the same attributes, but are closed.
    page closing tags are removed.
    """
    return re.sub(r'</page>', '', re.sub(r'<page( [^>]*)?>', r'<pb\1/>', data))


def close_bad_tags(tagnames, data):
    """
    Close all tags considered "bad" in the list of tagnames and remove any
    existing end tags.
    """
    newdata = data
    for tagname in tagnames:
        newdata = re.sub(r'</{}>'.format(tagname), '',
                         re.sub(r'(<{} [^>/]*)>'.format(tagname),
                                r'\1/>', newdata))
    return newdata


def infer_closing_tags(data):
    """
    Infer the closing tags for elements which cannot contain themselves,
    i.e. if two elements are adjacent and have the same tag but the first
    has no closing tag, add a closing tag before the second element.
    """
    return re.sub(r'(<(\w+)[^>]*>[^<]*)(<\2[^>]*>)', r'\1</\2>\3', data)


def fix_ampersands(data):
    """
    Replace all free ampersands with &amp;
    Free ampersands are those not part of an existing entity.
    Entities are found by the captured group and can have the following syntax:
    - &foo;
    - &#001;
    - &#xF01;
    """
    return re.sub(r'&([^;\s]*[^;\w#]|$)', r'&amp;\1', data)


def fix_typos(data):
    """
    Fix common typos in attributes
    - doubled quotation marks
    - missing quotation marks
    - missing spaces
    """
    newdata = re.sub(r'([^=])"[^=>\s]*">', r'\1">', data)
    newdata = re.sub(r'(="[^">]*)>', r'\1">', newdata)
    newdata = re.sub(r'(\w+="[^"]*")(\w+="[^"]*")', r'\1 \2', newdata)
    return newdata


def concat_lexemes(data):
    """
    Concatenate multiple lexeme attributes into one |-separated list.
    """
    #   replace all lexeme attribute pairs with LEXSTARTvalueLEXEND
    newdata = re.sub(r'( lexeme="([^"]+)")', r' LEXSTART\2LEXEND', data)
    # replace LEXEND LEXSTART text with a separator (|)
    newdata = re.sub(r'LEXEND\s+LEXSTART', r'|', newdata)
    # replace initial remaining LEXSTART with lexeme=",
    # final remaining LEXEND with "
    newdata = re.sub('LEXSTART', 'lexeme="', re.sub('LEXEND', '"', newdata))
    return newdata


def add_head_and_foot(data, dtdtext):
    """
    Add XML header and footer to data to resolve entities.
    """
    header = r'<?xml version="1.0" encoding="UTF-8" standalone="no"?>' \
        + r'<!DOCTYPE leme SYSTEM "leme.dtd"><root>'
    header = r'<?xml version="1.0" encoding="UTF-8"?>' + '\n'
    header += r'<!DOCTYPE leme [' + '\n' + dtdtext + '\n' + r']>'
    header += '\n' + r'<root>'
    footer = r'</root>'
    return header + data + footer


def preprocess(filename, dtdtext, outfilename):
    """
    Perform all preprocessing steps in order.
    """
    with open(filename, 'r') as inf:
        data = inf.read()
        data = create_pbs(data)
        data = close_bad_tags(['f', 'ornament'], data)
        data = fix_ampersands(data)
        data = fix_typos(data)
        data = concat_lexemes(data)
        data = add_head_and_foot(data, dtdtext)
        with open(outfilename, 'w+') as outf:
            outf.write(data)


if __name__ == "__main__":
    while True:
        txt_file = input("What is the name of the .txt file to be converted to an .xml file? ")
        print("Preprocessing...")
        with open('leme.dtd', 'r') as dtd:
            dtdtext = dtd.read()
        xml_file = txt_file[0:len(txt_file)-4]+'_prep.xml'
        preprocess(txt_file, dtdtext, xml_file)
        next_action = input("Press 'Enter' to exit the application, or type any other key to convert another file.  ")
        if next_action=="":
            break
