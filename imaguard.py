import numpy as np
from PIL import Image
import random
import os

def get_script_directory():
    """Get the directory of the script."""
    return os.path.dirname(os.path.abspath(__file__))

def encrypt_image(image_filename, output_filename='encrypted_image.png', key_filename='encryption_keys.npy'):
    script_dir = get_script_directory()
    
    # Read the original image
    image_path = os.path.join(script_dir, image_filename)
    img = Image.open(image_path)
    RGB = np.array(img)
    s = RGB.shape
    n = s[0] * s[1] * s[2]

    # Step 1: Randomly shuffle pixel points
    r = list(range(n))
    random.shuffle(r)  # Random sequence
    RGBS = RGB.reshape(-1)  # Convert the image to a one-dimensional array
    RGBSS = RGBS[r].reshape(s)  # Apply the random sequence to shuffle pixels

    # Step 2: Reset the three-dimensional data of the image
    Gadd = np.random.randint(0, 256, size=s, dtype=np.uint8)  # Generate a random matrix
    G1 = np.zeros_like(RGBSS, dtype=np.float32)

    # Encryption operation
    G1 = 0.1 * RGBSS + 0.9 * Gadd
    G1 = G1.astype(np.uint8)

    # Save the encrypted image and keys (random sequence and random matrix)
    encrypted_image_path = os.path.join(script_dir, output_filename)
    key_file_path = os.path.join(script_dir, key_filename)
    Image.fromarray(G1).save(encrypted_image_path)
    np.save(key_file_path, {'r': r, 'Gadd': Gadd})

def decrypt_image(input_filename='encrypted_image.png', key_filename='encryption_keys.npy', output_filename='decrypted_image.png'):
    script_dir = get_script_directory()
    
    # Load the encrypted image and keys
    input_path = os.path.join(script_dir, input_filename)
    key_file_path = os.path.join(script_dir, key_filename)
    G1 = np.array(Image.open(input_path))
    keys = np.load(key_file_path, allow_pickle=True).item()
    r = keys['r']
    Gadd = keys['Gadd']

    # Decryption operation
    G2 = (G1 - 0.9 * Gadd) / 0.1
    G2 = G2.clip(0, 255).astype(np.uint8)

    # Decrypt the image using the inverse index
    f = np.zeros_like(r)
    for t in range(len(r)):
        f[r[t]] = t
    RGBE = G2.reshape(-1)
    RGBEE = RGBE[f].reshape(G1.shape)

    # Save the decrypted image
    decrypted_image_path = os.path.join(script_dir, output_filename)
    Image.fromarray(RGBEE).save(decrypted_image_path)

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
