#!/usr/bin/env python
# -*- coding: utf-8 -*-

from InstagramAPI import InstagramAPI
import argparse

parser = argparse.ArgumentParser(description='Post something on Instagram')
parser.add_argument('-u', metavar='user', type=str,
                    help='Please enter your username')
parser.add_argument('-pw', metavar='password', type=str,
                    help='Please enter your password')
parser.add_argument('-t', metavar='text', type=str, default="text.txt",
                    help='Please the path to a text file')
parser.add_argument('-i', metavar='image', type=str, default="image.jpg",
                    help='Please the path to a imge file')

args = parser.parse_args()

try:
    InstagramAPI = InstagramAPI(args.u, args.pw)
    InstagramAPI.login()

    with open(args.t, 'r') as myfile:
        caption = myfile.read()

    InstagramAPI.uploadPhoto(args.i, caption=caption)
except Exeption as e:
    print(e)
    