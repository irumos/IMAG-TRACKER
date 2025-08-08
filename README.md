# IMAG-UPLOAD-TRACKER
To find the destination of the image which is uploaded in a website
# 🛡️ Image Upload Tracker

A simple Python tool to monitor image uploads from your device and identify where the image is sent on the network using Kali Linux tools like `tcpdump` and `scapy`.

## 📌 Features

- Captures network traffic during a file upload

- Analyzes `.pcap` files for HTTP POST requests involving image content

- Lists destination IPs where the image might be uploaded

- Optionally resolves IP addresses to domain names

## 🚀 How to Use

1. **Install Dependencies**:

   ```bash
   sudo apt install tcpdump
   pip install scapy

