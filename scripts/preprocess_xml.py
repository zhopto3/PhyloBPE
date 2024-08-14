"""Script to loop through all xml bibles, remove text, preprocess, and write to a plain text file
Zach Hopton
"""
import os
import xml.etree.ElementTree as ET
import re
import unicodedata


def preprocess(line):
    #get rid of casing
    line = line.lower()
    #get rid of some punctuation
    #Not removing apostrophes or dashes since those can be rather integral to orthography and sometimes sounds for apostrophes
    line = re.sub(r"""[\.,!?¡¿:;\(\)\[\]\{\}।”“"«»՝՜՛՞؛؟،]"""," ",line)
    #normalize hyphens, especially for afrikaans
    line = re.sub("--","-",line)
    line = re.sub(" - ","",line)
    #normalize spaces
    line = re.sub(r"\s+"," ",line)
    #do unicode normalization so diacritics are represented uniformaly 
    line = unicodedata.normalize("NFKC",line)
    return line+"\n"


def main():
    for f in os.listdir("./data/bible_xml"):
        out_name = f"{f.split('.')[0].split('-')[0]}.txt"

        #parse the xml version of the bibles
        with open(f"./data/bible_xml/{f}",'r',encoding='utf-8') as in_tree:
            full_str=in_tree.read()
            tree=ET.fromstring(full_str)

        with open(f"./data/bibles_clean/{out_name}","w",encoding='utf-8') as f_out:
            for verse in tree.iter("seg"):
                text = verse.text
                #filter empty lines
                if text:
                    text = preprocess(text)
                    f_out.write(text)


if __name__ == "__main__":
    main()