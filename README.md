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
