# QR Code Generator

This repository contains a simple script to generate a QR code from a given URL using the Python `qrcode` library.

## Description

The script allows you to create a QR code from a specified URL and save it as an image file. This can be useful for sharing links, contact information, or any other type of data that can be encoded in a QR code.

## Usage

1. **Install the required library:**

    Ensure you have the `qrcode` library installed. You can install it using pip:
    ```bash
    pip install qrcode[pil]
    ```

2. **Modify the URL:**

    Replace `"YOUR LINK"` in the script with the URL you want to encode into the QR code.

3. **Run the script:**

    Execute the script to generate the QR code and save it as `qrcode.png`.

    ```python
    import qrcode

    # QR CREATE
    url = "YOUR LINK"
    qr = qrcode.make(url)

    # QR SAVE
    qr.save("qrcode.png")
    ```

## Example

Replace `"YOUR LINK"` with `https://www.example.com` to create a QR code for the Example website:

```python
import qrcode

# QR CREATE
url = "https://www.example.com"
qr = qrcode.make(url)

# QR SAVE
qr.save("qrcode.png")
```

This will generate a QR code image and save it as `qrcode.png` in the current directory.
