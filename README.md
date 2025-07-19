# SMS CLI Tool for e-amarseba.com

This is a simple Python command-line interface (CLI) tool to interact with the `e-amarseba.com` Bulk SMS and SMS Tracking APIs. It allows you to send SMS messages and check their delivery status directly from your terminal.

**Important Security Note:** This tool requires your `x-app-key` and `x-app-secret`. For security, these are loaded from a `.env` file and should **never** be hardcoded directly into the script or shared publicly.

## Features

* **Send SMS:** Send messages to one or more contact numbers. (Does not use masking by default).

* **Track SMS:** Check the status of a sent SMS using its `track_id`.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

* **Python 3.x:** Download from [python.org](https://www.python.org/downloads/).

* **pip:** Python's package installer (usually comes with Python).

## Setup Instructions

Follow these steps to get the tool up and running:

### 1. Download the Script

* Save the `sms_cli.py` file to a directory on your computer (e.g., `D:\sms-project`).

### 2. Install Required Libraries

* Open your **terminal** (macOS/Linux) or **Command Prompt / PowerShell** (Windows).

* Navigate to the directory where you saved `sms_cli.py`. For example:

    ```
    cd D:\sms-project

    ```

* Install the necessary Python libraries using pip:

    ```
    pip install requests python-dotenv

    ```

### 3. Configure Your API Keys (`.env` file)

This is a **CRUCIAL** step for security and functionality.

* In the **same directory** where you saved `sms_cli.py` (e.g., `D:\sms-project`), create a new file named **exactly** `.env` (note the dot at the beginning and no file extension).

* Open this `.env` file with a plain text editor (like Notepad, VS Code, Sublime Text). **Do NOT use word processors like Microsoft Word.**

* Paste the following lines into the `.env` file, replacing `YOUR_X_APP_KEY_HERE` and `YOUR_X_APP_SECRET_HERE` with your actual API credentials obtained from your `e-amarseba.com` developer dashboard:

    ```
    SMS_API_KEY=YOUR_X_APP_KEY_HERE
    SMS_API_SECRET=YOUR_X_APP_SECRET_HERE

    ```

    * **Important:** Ensure there are **no extra spaces** before or after the `=` signs, or at the beginning/end of your key/secret values.

    * **Save** the `.env` file.

## How to Run the Tool

1.  **Open your terminal** and navigate to the directory where `sms_cli.py` and `.env` are located (e.g., `D:\sms-project`).

    ```
    cd D:\sms-project

    ```

2.  **Run the Python script:**

    ```
    python sms_cli.py

    ```

    (If `python` doesn't work, try `python3 sms_cli.py`)

## Using the Tool

Once the script starts, you will see a menu:

![Send SMS Screenshot](https://raw.githubusercontent.com/AbrarBb/SMS-API/main/Screen/Send.jpg)
![Track Result Screenshot](https://raw.githubusercontent.com/AbrarBb/SMS-API/main/Screen/Track_result.jpg)
