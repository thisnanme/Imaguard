# Imaguard
### Project Description: Imaguard

**Imaguard** is a Python-based tool designed for educational and recreational purposes, allowing users to experiment with basic image encryption and decryption techniques. By combining two fundamental methods—pixel shuffling and three-dimensional data resetting—Imaguard offers an engaging way to explore the principles of image cryptography. However, it is important to note that this method does not provide robust security and should not be relied upon for protecting sensitive or confidential information.

#### Key Features:
- **Pixel Shuffling:** The original image's pixels are randomly rearranged, resulting in an encrypted image that appears as noise or random patterns.
- **Three-Dimensional Data Resetting:** A random matrix is applied to the RGB values of the image, further obscuring the original content.
- **Key Management:** Encryption keys, including the shuffle sequence and the random matrix, are saved separately, ensuring that only those with access to both the encrypted image and the key can restore the original image.
- **Ease of Use:** Simple function calls allow users to easily encrypt and decrypt images without requiring extensive knowledge of cryptography.
- **Cross-Platform Compatibility:** Built on Python, Imaguard can run on any operating system where Python is supported.

#### Intended Use Cases:
- **Personal Sharing:** Individuals can use Imaguard for casual sharing of personal photos with friends or family over social media platforms.
- **Educational Purposes:** Students and educators can utilize this tool to learn about basic concepts of image encryption and decryption in a practical setting.

#### Important Security Note:
It is crucial to understand that the encryption method implemented by Imaguard is **not suitable for secure transmission of sensitive or confidential data**. For actual security requirements, professional-grade encryption algorithms and protocols should be employed. This tool is intended solely for personal, non-critical applications and educational exploration.

#### How It Works:
1. **Encryption Process:** Users provide an image file to be encrypted. Imaguard applies pixel shuffling followed by three-dimensional data resetting, generating an encrypted image and saving the necessary keys for decryption.
2. **Decryption Process:** With the encrypted image and corresponding keys, users can restore the original image by reversing the encryption steps.
