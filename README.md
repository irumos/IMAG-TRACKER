# IMAGE-TRACKER
To find the destination of the image which is uploaded in a website
#   Image Tracker

A simple Python tool to monitor image uploads from your device and identify where the image is sent on the network using Kali Linux tools like `tcpdump` and `scapy`.

##  Features

- Captures network traffic during a file upload

- Analyzes `.pcap` files for HTTP POST requests involving image content

- Lists destination IPs where the image might be uploaded

- Optionally resolves IP addresses to domain names

## How to Use the Tool

-> Step 1: Open Your Terminal

Navigate to the folder where you saved the files:
cd image-upload-tracker

-> Step 2: Run the Script

Use sudo to allow network capture
sudo python3 image_tracker.py

-> Example:

--- Image Tracker ---
Enter network interface to monitor (e.g., wlan0): wlan0
Enter duration of capture in seconds: 15
During this 15-second window, upload an image using a browser or an app.

-> Step 4: Upload Your Image During Capture

Quickly open the target app or site (e.g., WhatsApp Web, Facebook, or a test form) and upload your image.

⚠️ You need to start uploading during the active capture window.

-> Step 5: View Results

After capture, the tool will analyze the traffic and show:

The IP addresses involved

Domains they map to (if found)
