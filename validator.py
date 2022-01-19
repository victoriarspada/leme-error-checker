
"""
LEME Validation program of XML files.

Author: Victoria Spada
Contact_ victoria.spada@mail.utoronto.ca
Last Edit: Fri Jan 29 2021.
"""
import os 
from lxml import etree

def validator(xml_path: str, xsd_path: str) -> bool:
    result = False
    xmlschema_doc = etree.parse(xsd_path)
    xmlschema = etree.XMLSchema(xmlschema_doc)

    # Destination of error logs
    error_schema = 'logs/error_schema.log'  
    error_syntax = 'logs/error_syntax.log'  

    # Parse the xml document.
    try:
        xml_doc = etree.parse(xml_path)
        print('XML well formed, syntax ok.')
        result = xmlschema.validate(xml_doc)
        # Validate the parsed file against the XSD.
        try:
            xmlschema.assertValid(xml_doc)
            print('Encoding valid, schema validation ok.')

        except etree.DocumentInvalid as error:
            print('Schema validation error, see error_schema.log')
            with open(error_schema, 'w') as error_log_file:
                error_log_file.write(str(error.error_log))

        except:
            print("Unknown error. Exiting...")
      
    except etree.XMLSyntaxError as error:
        print('XML Syntax Error, see error_syntax.log')
        with open(error_syntax, 'w') as error_log_file:
            error_log_file.write(str(error.error_log))
            
    except:
        print("Unknown error. Exiting...")

    return result


