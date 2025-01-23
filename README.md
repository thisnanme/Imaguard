# Imaguard
**Imaguard** is an innovative Python-based tool designed to securely encrypt and decrypt images, ensuring the confidentiality of visual content when shared over potentially insecure channels. This project combines two fundamental image encryption methods—pixel shuffling and three-dimensional data resetting—to provide a robust yet straightforward solution for protecting sensitive images.

#### Key Features:
- **Pixel Shuffling:** The original image's pixels are randomly rearranged, making the encrypted image appear as noise or random patterns.
- **Three-Dimensional Data Resetting:** A random matrix is applied to the RGB values of the image, further obscuring the original content.
- **Secure Key Management:** Encryption keys, including the shuffle sequence and the random matrix, are saved separately, ensuring that only those with access to both the encrypted image and the key can restore the original image.
- **User-Friendly Interface:** Simple function calls allow users to easily encrypt and decrypt images without needing deep knowledge of cryptography.
- **Platform Independence:** Since it's built on Python, Imaguard can run on any operating system where Python is supported, offering broad compatibility.

#### Use Cases:
- **Private Sharing:** Individuals can use Imaguard to safely share personal photos with friends or family members over public networks.
- **Professional Applications:** Businesses can leverage this tool to protect proprietary graphics or confidential visual information from unauthorized access.
- **Educational Purposes:** Students and educators can explore basic concepts of image encryption and decryption in a practical setting.

#### How It Works:
1. **Encryption Process:** Users provide an image file to be encrypted. Imaguard applies pixel shuffling followed by three-dimensional data resetting, generating an encrypted image and saving the necessary keys for decryption.
2. **Decryption Process:** With the encrypted image and corresponding keys, users can restore the original image by reversing the encryption steps.

#### Why Choose Imaguard?
Imaguard stands out for its simplicity and effectiveness. By combining proven encryption techniques, it offers a balance between security and ease of use. Whether you're looking to safeguard your personal memories or ensure corporate compliance, Imaguard provides a reliable method to protect your images.
