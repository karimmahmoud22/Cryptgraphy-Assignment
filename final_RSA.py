import random
from math import sqrt
import matplotlib.pyplot as plt
import time
from functools import reduce
from sympy.ntheory.modular import crt
from math import gcd
import sympy.ntheory as nt
from Cryptodome.Util import number

# find the greatest common divisor of two numbers
def gcd(a, b):

    while b != 0:
        temp = b
        b = a % b
        a = temp

    return a
   
#generata public and private keys for RSA
def generate_key_pair(number_of_bits):

    # Generate two large random prime numbers p and q
    p = number.getPrime(number_of_bits)
    q = number.getPrime(number_of_bits)

    while ( q == p):
        q = number.getPrime(number_of_bits)
    
    # Compute n = p * q
    # Compute phi(n) = (p - 1) * (q - 1)
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Find an integer e such that 1 < e < phi and gcd(e, phi) = 1
    while True:
        e = random.randrange(2 ** number_of_bits, phi)
        if gcd(e, phi) == 1:
            break
    
    # Compute d such that e * d ≡ 1 (mod phi)
    d = inverse_mod(e, phi)
    
    # Return the public key (n, e) and the private key (n, d)
    return (n, e), (n, d)

# find the inverse of a number
def inverse_mod(a, m):

    if gcd(a, m) != 1:
        return None
    
    # Calculate using the Extended Euclidean Algorithm:
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    
    while v3 != 0:
        q = u3 // v3 
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3

    return u1 % m

# the alphabet conversion
alphabet = '0123456789abcdefghijklmnopqrstuvwxyz '

# convert a message to a number
def encode_message(msg):

    # Convert any extra characters to spaces
    msg = msg.lower()
    msg = ''.join([c if c in alphabet else ' ' for c in msg])

    # Group the plaintext into sets of five characters per group
    groups = [msg[i:i+5] for i in range(0, len(msg), 5)]

    # Append space to the last group if it's not exactly five characters
    if len(groups[-1]) < 5:
        groups[-1] += ' '*(5-len(groups[-1]))

    # Convert each group into a separate number
    num = 0
    for group in groups:
        for c in group:
            num *= 37
            num += alphabet.index(c)

    return num

# convert a number to a message
def decode_message(num):
    
    nums = []
    
    while num > 0:
        nums.append(num % 37)
        num //= 37
    plaintext = ''.join(alphabet[num] for num in nums[::-1])
    
    return plaintext.rstrip()

# encrypt a message
def encrypt(plaintext, public_key):
    
    n, e = public_key
    num = encode_message(plaintext)

    return pow(num, e, n)

# decrypt a message
def decrypt(ciphertext, private_key):

    n, d = private_key
    num = pow(ciphertext, d, n)

    return decode_message(num)


# test the functions
def test():

    # Generate key pair
    public_key, private_key = generate_key_pair(100)
    
    # Encrypt a message
    plaintext = 'karim mahmoud kamal'
    ciphertext = encrypt(plaintext, public_key)
    print('Ciphertext:', ciphertext)
    
    # Decrypt the message
    decrypted_plaintext = decrypt(ciphertext, private_key)
    print('Decrypted plaintext:', decrypted_plaintext)


# A graph consisting of the number of bits in generated_key_pair on x axis and the time it takes to encrypt a message of 5 characters on y axis
def graph():
    x = []
    y1 = []
    y2 = []

    for i in range(3, 1024):

        public_key, private_key = generate_key_pair(i)

        start_enc = time.time()
        encry = encrypt('hi s7', public_key)
        end_enc = time.time()
        
        start_dec = time.time()
        decrypt(encry, private_key)
        end_dec = time.time()
        
        x.append(i)
        y1.append(end_enc - start_enc)
        y2.append(end_dec - start_dec)
        
    plt.xlabel('Number of bits')
    plt.ylabel('Encryption Time')
    plt.plot(x, y1)
    plt.show()
    plt.figure(1)

    plt.xlabel('Number of bits')
    plt.ylabel('Decryption Time')
    plt.plot(x, y2)
    plt.show()
    plt.figure(2)
    

# break RSA using the brute force method
def break_rsa(public_key):
    n, e = public_key
    p = 0
    q = 0
    for i in range(2, n):
        if n % i == 0:
            p = i
            q = n // i
            break
    phi = (p - 1) * (q - 1)
    d = inverse_mod(e, phi)
    return (n, d)

# A graph consisting of the number of bits in generated_key_pair on x axis and the time it takes to break RSA on y axis
def break_rsa_graph():
    x = []
    y1 = []
    
    for i in range(3, 32):
        public_key, private_key = generate_key_pair(i)

        start_break = time.time()
        print('break_rsa(public_key):', break_rsa(public_key))
        end_break = time.time()
        
        x.append(i)
        y1.append(end_break - start_break)

    plt.xlabel('Number of bits')
    plt.ylabel('Attack Time')
    plt.plot(x, y1)
    plt.show()
    plt.figure(1)    

#if __name__ == '__main__':
    #test()
    #graph()
    #public_key, private_key = generate_key_pair(4)
    #print('public_key:', public_key)
    #print('private_key:', private_key)
    #print('break_rsa(public_key):', break_rsa(public_key))
    #generate_key_pairs()
    