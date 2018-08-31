import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-E","--Encrypt",help ="Enter The encryption text")
parser.add_argument("-D","--Decrypt",help ="Enter The decryption text")
args = parser.parse_args()

key = 26
plaintext=""



# encipher

if(args.Encrypt):
	for x in range(key):
		ciphertext = ""
		plaintext = args.Encrypt
		for c in plaintext:
			if(c.isalpha()):

				if ((c>='a' and c<=chr(ord('z')-x)) or (c<=chr(ord('Z')-x) and c>='A')):
					ciphertext = ciphertext+chr((ord(c)+x))
				else:
					ciphertext = ciphertext+chr((ord(c)+x)-26)
			else:
				plaintext2 += c
		print ciphertext	
# decipher

if (args.Decrypt):
	for x in range(key):
		plaintext2 = ""
		ciphertext = args.Decrypt
		for c in ciphertext:
			if(c.isalpha()):
				if ((c>=chr(ord('a')+x) and c<='z') or (c<='Z' and (c>=chr(ord('A')+x)))):
					plaintext2 = plaintext2+chr((ord(c)-x))
				else:
					plaintext2 = plaintext2+chr((ord(c)-x)+26)
			else:
				plaintext2 += c
		print plaintext2
#print plaintext

