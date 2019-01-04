import base64

text = input("Enter a text: ")
print("Encoded text: "  + base64.b64encode(bytes(text,'utf-8')))
print("Decoded text: " + base64.b64decode(bytes(text,'utf-8')))