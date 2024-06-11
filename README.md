# Cryptgraphy-Assignment

# RSA Assignment

## Description

RSA (Rivest–Shamir–Adleman) is a public-key cryptosystem widely used for secure data transmission. In a public-key cryptosystem, the encryption key is public and distinct from the decryption key, which is kept secret (private). An RSA user creates and publishes a public key based on two large prime numbers, along with an auxiliary value. The prime numbers are kept secret. Messages can be encrypted by anyone using the public key but can only be decoded by someone who knows the prime numbers. 

The security of RSA relies on the practical difficulty of factoring the product of two large prime numbers, known as the "factoring problem." There are no published methods to defeat the system if a large enough key is used. This project aims to demonstrate how RSA works and illustrate the difficulty of breaking it.

### Objectives

- Build a program that can encrypt and decrypt text using the RSA algorithm.
- Implement another program that attempts to break RSA and retrieve the correct private key.
- Analyze different key sizes (number of bits of \( n \)) and their effects on the speed of encryption/decryption and the time taken to break the algorithm.

## Alphabet Conversion

We will use a specific alphabet conversion for encoding messages:
- **0-9**: Return their value (e.g., 0→0, 5→5, 9→9)
- **a-z**: Map to 10-35 (e.g., a→10, b→11, ..., z→35)
- **Space**: Maps to 36

Only these 37 characters will be used for messages. Treat any other characters as spaces (assigned the value of 36).

### Character Conversion

Before implementing RSA, encode the input message as a number using the following scheme:
1. Convert extra characters to spaces as specified above.
2. Group the plaintext into sets of five characters. Append spaces to the end if the last group has fewer than five characters.
3. Convert each group into a separate number. If the grouping is \([c_4, c_3, c_2, c_1, c_0]\), then the number is:

\[ \sum_{i=0}^{4} c_i \cdot 37^i \]

#### Example

Assume our plaintext grouping is \([h i \space s 7]\). Translate the characters into numbers:
- \(c_4 = h = 17\)
- \(c_3 = i = 18\)
- \(c_2 = \space = 36\)
- \(c_1 = s = 28\)
- \(c_0 = 7 = 7\)

Then compute the plaintext number:

\[ 17 \cdot 37^4 + 18 \cdot 37^3 + 36 \cdot 37^2 + 28 \cdot 37^1 + 7 = 32,822,818 \]

Decoding should reverse this process.
