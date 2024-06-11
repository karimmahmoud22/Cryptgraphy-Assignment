from final_RSA import generate_key_pair as generate_key_pair1

# Generate a public/private key pair for the client
public_key_c, private_key_c = generate_key_pair1(1024)

# Generate a public/private key pair for the server
public_key_s, private_key_s = generate_key_pair1(1024)

f = open("keys.txt", "a")

f.write(str(public_key_c[0]) + '\n')
f.write(str(public_key_c[1]) + '\n')

f.write(str(private_key_s[0]) + '\n')
f.write(str(private_key_s[1]) + '\n')

f.write(str(public_key_s[0]) + '\n')
f.write(str(public_key_s[1]) + '\n')

f.write(str(private_key_c[0]) + '\n')
f.write(str(private_key_c[1]) + '\n')

f.close()