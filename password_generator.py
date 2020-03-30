#!/usr/bin/python3

import argparse
import random
import string

def generate_password(
    count,
    allow_lower=True, allow_upper=True,
    allow_digit=True, allow_punctuation=True):
    
    characters = ""

    if allow_lower:
        characters += string.ascii_lowercase
    if allow_upper:
        characters += string.ascii_uppercase
    if allow_digit:
        characters += string.digits
    if allow_punctuation:
        characters += string.punctuation
        
    password = ""
    for i in range(args.count):
        password += random.choice(characters)

    return password

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--count", "-c", type=int, default=8, help="Password length")
    parser.add_argument(
        "--no-lowercase", "-l", dest="allow_lower", action="store_false",
        help="Do no include lowercase letters")
    parser.add_argument(
        "--no-uppercase", "-u", dest="allow_upper", action="store_false",
        help="Do no include uppercase letters")
    parser.add_argument(
        "--no-digit", "-d", dest="allow_digit", action="store_false",
        help="Do no include digits")
    parser.add_argument(
        "--no-punctuation", "-p", dest="allow_punctuation",
        action="store_false", help="Do no include punctuation signs")
    
    args = parser.parse_args()
   
    password = generate_password(
        args.count, args.allow_lower, args.allow_upper, args.allow_digit,
        args.allow_punctuation)
        
    print(password)