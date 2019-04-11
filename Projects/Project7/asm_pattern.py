"""Temp testing new pattern"""
import re

ASM_FULL_SYM = re.compile(r"""
   # Optional label 
   (
     (?P<label> [a-zA-Z]\w*):
   )?
   # The instruction proper 
   \s*
    (?P<opcode>    (JUMP)|(STORE)|(LOAD))           # Opcode
    (/ (?P<predicate> [a-zA-Z]+) )?                 # Predicate (optional)
    \s+
    ((?P<target>    r[0-9]+),)?                     # Target register (optional)
    (?P<symbol>     [a-zA-Z]\w*)
    
   # Optional comment follows # or ; 
   (
     \s*
     (?P<comment>[\#;].*)
   )?       
   \s*$             
   """, re.VERBOSE)

def test_match(s: str):
    match = ASM_FULL_SYM.match(s)

    if match:
        print("Matched {}, \nfields {}".format(s,match.groupdict()))
    else:
        print("Didn't match {}".format(s))


test_match("lab: JUMP/Z foo")
test_match("   JUMP/Z foo")
test_match("   LOAD r0,foo")
test_match("STORE r1,bar")



