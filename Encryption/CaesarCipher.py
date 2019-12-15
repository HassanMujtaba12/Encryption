import base64 

def encrypt(string, shift):
    shift = int(shift)
    cipher = ''
    for char in string: 
        if char == ' ':
          cipher = cipher + char
        elif  char.isupper():
          cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
        else:
          cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
    return cipher
def decrypt(string, shift):
  shift = int(shift)
  cipher=''
  for char in string: 
    if char == ' ':
      cipher = cipher + char
    elif  char.isupper():
      cipher = cipher + chr((ord(char) - shift - 65) % 26 + 65)
    else:
      cipher = cipher + chr((ord(char) - shift - 97) % 26 + 97)
  return cipher

def veg_encode(key, clear): 
    enc = [] 
      
    for i in range(len(clear)): 
        key_c = key[i % len(key)] 
        enc_c = chr((ord(clear[i]) +
                     ord(key_c)) % 256) 
                       
        enc.append(enc_c) 
          
    return base64.urlsafe_b64encode("".join(enc).encode()).decode() 
  
# Function to decode 
def veg_decode(key, enc): 
    dec = [] 
      
    enc = base64.urlsafe_b64decode(enc).decode() 
    for i in range(len(enc)): 
        key_c = key[i % len(key)] 
        dec_c = chr((256 + ord(enc[i]) -
                           ord(key_c)) % 256) 
                             
        dec.append(dec_c) 
    return "".join(dec) 

def encryptMessage(text,key):
    """ Returns the Vernam Cypher for given string and key """
    answer = "" # the Cypher text
    p = 0 # pointer for the key
    for char in text:
        answer += chr(ord(char) ^ ord(key[p]))
        p += 1
        if p==len(key):
            p = 0
    return answer

#s='nasah si siht'
#print(encryptMessage(s))
"""

#text = input("enter string: ")
#s = int(input("enter shift number: "))
#g=encrypt(text,s)
#print(g)
"""
