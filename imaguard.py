"""
Project: Imaguard
File: imaguard.py
Author: thisname <https://github.com/thisnanme>
Date: February 5, 2025
Copyright Notice: Copyright © 2025 thisname. All rights reserved.
Description: 
    Imaguard is a Python tool that securely encrypts and decrypts images using pixel shuffling and three-dimensional data resetting, protecting visual content privacy.
"""
import numpy as np
from PIL import Image
import secrets
import random
import os

def get_script_directory():
    """Get the directory of the script."""
    return os.path.dirname(os.path.abspath(__file__))

def encrypt_image(image_filename, output_filename='encrypted_image.png', key_filename='encryption_keys.npy'):
    script_dir = get_script_directory()
    
    # Load the original image
    image_path = os.path.join(script_dir, image_filename)
    img = Image.open(image_path)
    rgb_array = np.array(img)
    shape = rgb_array.shape
    total_pixels = shape[0] * shape[1] * shape[2]

    # Generate a secure seed and initialize a random generator with it
    secure_seed = secrets.randbits(32)
    rng = random.Random(secure_seed)

    # Step 1: Shuffle pixels
    shuffle_sequence = list(range(total_pixels))
    rng.shuffle(shuffle_sequence)  # Use the secure random generator to shuffle
    flattened_rgb = rgb_array.reshape(-1)  # Convert image to a 1D array
    shuffled_rgb = flattened_rgb[shuffle_sequence].reshape(shape)  # Apply random sequence to shuffle pixels

    # Step 2: Three-dimensional data resetting
    random_matrix = np.random.RandomState(seed=secure_seed).randint(0, 256, size=shape, dtype=np.uint8)  # Generate a random matrix using the same seed
    encrypted_image = np.zeros_like(shuffled_rgb, dtype=np.float32)

    # Encryption operation
    encrypted_image = 0.1 * shuffled_rgb + 0.9 * random_matrix
    encrypted_image = encrypted_image.astype(np.uint8)

    # Save the encrypted image and keys (random sequence and random matrix)
    encrypted_image_path = os.path.join(script_dir, output_filename)
    key_file_path = os.path.join(script_dir, key_filename)
    Image.fromarray(encrypted_image).save(encrypted_image_path)
    np.save(key_file_path, {'shuffle_sequence': shuffle_sequence, 'random_matrix': random_matrix})

def decrypt_image(input_filename='encrypted_image.png', key_filename='encryption_keys.npy', output_filename='decrypted_image.png'):
    script_dir = get_script_directory()
    
    # Load the encrypted image and keys
    input_path = os.path.join(script_dir, input_filename)
    key_file_path = os.path.join(script_dir, key_filename)
    encrypted_image = np.array(Image.open(input_path))
    keys = np.load(key_file_path, allow_pickle=True).item()
    shuffle_sequence = keys['shuffle_sequence']
    random_matrix = keys['random_matrix']

    # Decryption operation
    decrypted_image = (encrypted_image - 0.9 * random_matrix) / 0.1
    decrypted_image = decrypted_image.clip(0, 255).astype(np.uint8)

    # Restore pixel order using the inverse of the shuffle sequence
    inverse_shuffle = np.zeros_like(shuffle_sequence)
    for t in range(len(shuffle_sequence)):
        inverse_shuffle[shuffle_sequence[t]] = t
    flattened_decrypted = decrypted_image.reshape(-1)
    restored_rgb = flattened_decrypted[inverse_shuffle].reshape(encrypted_image.shape)

    # Save the decrypted image
    decrypted_image_path = os.path.join(script_dir, output_filename)
    Image.fromarray(restored_rgb).save(decrypted_image_path)

def main():
    script_dir = get_script_directory()
    
    print("Please choose an option:")
    print("1. Encrypt an image")
    print("2. Decrypt an image")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        original_image_path = os.path.join(script_dir, 'original_image.png')
        if not os.path.exists(original_image_path):
            print(f"The file {original_image_path} does not exist.")
            return
        encrypt_image('original_image.png')
        print("Image encrypted successfully.")

    elif choice == '2':
        encrypted_image_path = os.path.join(script_dir, 'encrypted_image.png')
        key_file_path = os.path.join(script_dir, 'encryption_keys.npy')
        if not (os.path.exists(encrypted_image_path) and os.path.exists(key_file_path)):
            print("Either the encrypted image or the key file does not exist.")
            return
        decrypt_image()
        print("Image decrypted successfully.")

    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
