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
