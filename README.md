# Pengolahan_Citra_PER13
```
FEBRIYANI NURHIDA
312210222
```

## STEGANOGRAFI DAN WATERMARKING

KODE :

```
from PIL import Image

def hide_text(image_path, secret_text, output_path):
    # Open the image
    image = Image.open(image_path)
    
    # Convert secret text to binary
    binary_secret_text = ''.join(format(ord(char), '08b') for char in secret_text)
    
    # Check if the image can accommodate the secret text
    image_capacity = image.width * image.height * 3
    if len(binary_secret_text) > image_capacity:
        raise ValueError("Image does not have sufficient capacity to hide the secret text.")
    
    # Hide the secret text in the image 
    pixels = image.load()
    index = 0
    for i in range(image.width):
        for j in range(image.height):
            pixel = pixels[i, j]
            if len(pixel) == 4:  # RGBA format
                r, g, b, a = pixel
            else:  # RGB format
                r, g, b = pixel
            
            # Modify the least significant bit of each color channel
            if index < len(binary_secret_text):
                r = (r & 0xFE) | int(binary_secret_text[index])
                index += 1
            if index < len(binary_secret_text):
                g = (g & 0xFE) | int(binary_secret_text[index])
                index += 1
            if index < len(binary_secret_text):
                b = (b & 0xFE) | int(binary_secret_text[index])
                index += 1
            
            if len(pixel) == 4:  # Update pixel with alpha channel
                pixels[i, j] = (r, g, b, a)
            else:  # Update pixel without alpha channel
                pixels[i, j] = (r, g, b)
    
    # Save the image with the hidden text
    image.save(output_path)

def extract_text(image_path):
    # Open the image
    image = Image.open(image_path)
    
    # Extract the secret text from the image
    pixels = image.load()
    binary_secret_text = ""
    for i in range(image.width):
        for j in range(image.height):
            pixel = pixels[i, j]
            if len(pixel) == 4:  # RGBA format
                r, g, b, a = pixel
            else:  # RGB format
                r, g, b = pixel
            
            # Extract the least significant bit from each color channel
            binary_secret_text += str(r & 1)
            binary_secret_text += str(g & 1)
            binary_secret_text += str(b & 1)
    
    # Convert binary text to ASCII
    secret_text = ""
    for i in range(0, len(binary_secret_text), 8):
        byte = binary_secret_text[i:i+8]
        if len(byte) < 8:
            break
        char = chr(int(byte, 2))
        secret_text += char
    
    return secret_text

# Image paths and secret text
image_path = 'D:\\Perkuliahan\\semester4\\pengolahan_citra\\data\\bananaref.png'
secret_text = 'This is a secret message.'
output_path = 'output_image.png'

# Hide the secret text in the image
hide_text(image_path, secret_text, output_path)

# Extract the secret text from the image
extracted_text = extract_text(output_path)
print("Extracted text:", extracted_text)
```

kode ini di simpan di file bernama secret.py
![ss1](https://github.com/Febriyaninurhida123/Pengolahan_Citra_PER13/assets/90132092/8eb2c089-e383-4eda-8b58-6526ac433750)


kemudian Pastikan Anda memiliki gambar yang ingin Anda gunakan untuk menyimpan pesan rahasia dan gambar untuk menyimpannya (misalnya, image.jpg). Pastikan juga path yang Anda gunakan dalam kode sesuai dengan lokasi gambar yang sebenarnya di sistem Anda.

Jalankan script Python Anda dengan menggunakan perintah seperti ini di terminal atau command prompt Anda:

```
python secret.py
```
Setelah dijalankan, program akan menyembunyikan pesan rahasia ke dalam gambar yang disebutkan, dan menyimpannya dengan nama yang ditentukan dalam variabel output_path. Jika tidak ada error, gambar baru akan disimpan di lokasi yang sama dengan script Python Anda.

Setelah itu, program akan mengekstrak pesan rahasia dari gambar yang baru dibuat dan mencetaknya di terminal atau command prompt.
![pengolahan_citra_per13](https://github.com/Febriyaninurhida123/Pengolahan_Citra_PER13/assets/90132092/c2398300-7cca-40fe-ac0b-95984c84dc6d)

