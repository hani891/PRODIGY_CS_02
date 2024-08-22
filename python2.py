from PIL import Image
import random

def encrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    pixels = image.load()

    # Iterate through each pixel
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            # Get the RGB values of the pixel
            r, g, b = pixels[i, j]
            
            # Apply a simple encryption by adding the key value to each RGB component
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256
            
            # Update the pixel with the new value
            pixels[i, j] = (r, g, b)

    # Save the encrypted image
    image.save(output_path)

def decrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    pixels = image.load()

    # Iterate through each pixel
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            # Get the RGB values of the pixel
            r, g, b = pixels[i, j]
            
            # Reverse the encryption by subtracting the key value
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256
            
            # Update the pixel with the new value
            pixels[i, j] = (r, g, b)

    # Save the decrypted image
    image.save(output_path)

# Input from user
image_path = input("Enter the path of the image to encrypt: ")
output_path_encrypted = "encrypted_image.png"
output_path_decrypted = "decrypted_image.png"
key = int(input("Enter the encryption key (integer): "))

# Encrypt the image
encrypt_image(image_path, output_path_encrypted, key)
print(f"Encrypted image saved as {output_path_encrypted}")

# Decrypt the image
decrypt_image(output_path_encrypted, output_path_decrypted, key)
print(f"Decrypted image saved as {output_path_decrypted}")
