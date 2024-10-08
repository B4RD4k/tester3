import gzip
import io

# ASCII characters representing compressed data
ascii_chars = [31,139,8,0,0,0,0,0,0,3,157,144,93,11,194,32,20,134,255,203,185,150,216,110,247,87,214,16,231,172,9,78,203,115,132,125,224,127,239,24,43,10,34,34,47,84,94,125,30,94,221,0,67,36,104,218,13,36,234,16,13,52,48,24,212,71,200,34,207,51,207,143,188,19,112,77,38,46,208,108,208,135,224,202,122,178,142,76,100,154,15,113,12,201,13,119,211,164,72,143,82,185,114,39,103,177,7,5,32,75,206,148,205,174,130,62,161,245,6,81,234,224,49,57,82,158,32,191,51,165,78,180,23,178,193,255,70,114,165,9,247,154,200,111,171,14,85,45,128,212,153,195,246,201,129,128,23,82,124,244,117,95,124,214,15,9,41,46,242,79,113,113,3,218,149,191,163,174,120,228,27,133,62,35,37,139,1,0,0]

# Convert ASCII values to bytes
compressed_data = bytes(ascii_chars)

# Decompress the data
with gzip.GzipFile(fileobj=io.BytesIO(compressed_data), mode='rb') as f:
    decompressed_data = f.read()

# Convert bytes to string
original_string = decompressed_data.decode('utf-8')

# Print the original string
print(original_string)
