import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
# This must be called before accessing os.getenv()
load_dotenv()

# --- Configuration ---
# API Keys: Loaded from environment variables for security.
# If not found, it will default to 'YOUR_X_APP_KEY_HERE' (for demonstration only).
# In production, ensure these are properly set in your environment or .env file.
API_KEY = os.getenv('SMS_API_KEY', 'YOUR_X_APP_KEY_HERE')
API_SECRET = os.getenv('SMS_API_SECRET', 'YOUR_X_APP_SECRET_HERE')

# --- DEBUGGING LINES START HERE ---
# These lines will print the API keys that the script is actually using.
# Check this output carefully to ensure your keys are loaded correctly from .env.
print(f"\n--- Debugging API Keys ---")
print(f"API_KEY loaded: '{API_KEY}'")
print(f"API_SECRET loaded: '{API_SECRET}'")
print(f"--- End Debugging ---")

# Check if API keys are still placeholders after loading from .env
if API_KEY == 'YOUR_X_APP_KEY_HERE' or API_SECRET == 'YOUR_X_APP_SECRET_HERE':
    print("\nWARNING: API keys are still placeholders or not loaded correctly from environment variables/ .env file.")
    print("Please ensure your .env file is in the same directory and contains your actual keys:")
    print("SMS_API_KEY=YOUR_ACTUAL_APP_KEY")
    print("SMS_API_SECRET=YOUR_ACTUAL_APP_SECRET")
    print("SMS sending/tracking will likely fail until this is corrected.")
# --- DEBUGGING LINES END HERE ---


# API Endpoints
SEND_SMS_ENDPOINT = 'https://e-amarseba.com/api/v1/http/services/bulk-sms/send-sms'
TRACK_SMS_ENDPOINT = 'https://e-amarseba.com/api/v1/http/services/bulk-sms/track-sms'

def send_sms(contacts, text):
    """
    Sends an SMS message to the specified contacts using the e-amarseba.com API.
    This version explicitly does NOT use masking.

    Args:
        contacts (list): A list of phone numbers (strings).
        text (str): The message text.

    Returns:
        dict: The JSON response from the API, or an error dictionary.
    """
    headers = {
        'x-app-key': API_KEY,
        'x-app-secret': API_SECRET,
        'Content-Type': 'application/json'
    }

    # Explicitly set is_masking to False and masking_name to None
    is_masking = False
    masking_name = None

    payload = {
        'contacts': contacts,
        'text': text,
        'is_masking': is_masking,
        'masking_name': masking_name
    }

    print(f"\n--- Sending SMS ---")
    print(f"Attempting to send SMS to: {contacts}")
    print(f"Message: '{text}'")
    print(f"Using masking: {'Yes' if is_masking else 'No'}") # Will always print 'No' now

    try:
        response = requests.post(SEND_SMS_ENDPOINT, headers=headers, json=payload)
        response.raise_for_status() # Raise an exception for HTTP errors (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error sending SMS: {e}")
        if hasattr(response, 'text'):
            print(f"Response content: {response.text}")
        return {"success": False, "message": f"Request failed: {e}"}
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response for send SMS: {e}")
        print(f"Raw response text: {response.text}")
        return {"success": False, "message": f"Invalid JSON response: {e}"}

def track_sms(track_id):
    """
    Tracks the status of an SMS message using its track_id via the e-amarseba.com API.

    Args:
        track_id (str): The track ID of the SMS to query.

    Returns:
        dict: The JSON response from the API, or an error dictionary.
    """
    headers = {
        'x-app-key': API_KEY,
        'x-app-secret': API_SECRET,
        'Content-Type': 'application/json'
    }

    payload = {
        'track_id': track_id
    }

    print(f"\n--- Tracking SMS ---")
    print(f"Attempting to track SMS with ID: {track_id}")

    try:
        response = requests.post(TRACK_SMS_ENDPOINT, headers=headers, json=payload)
        response.raise_for_status() # Raise an exception for HTTP errors (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error tracking SMS: {e}")
        if hasattr(response, 'text'):
            print(f"Response content: {response.text}")
        return {"success": False, "message": f"Request failed: {e}"}
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response for track SMS: {e}")
        print(f"Raw response text: {response.text}")
        return {"success": False, "message": f"Invalid JSON response: {e}"}

def main_menu():
    """Displays the main menu and handles user choices."""
    while True:
        print("\n--- SMS Service Menu ---")
        print("1. Send SMS")
        print("2. Track SMS")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            contacts_input = input("Enter contacts (comma-separated, e.g., 01712345678,01898765432): ")
            contacts = [c.strip() for c in contacts_input.split(',') if c.strip()]
            if not contacts:
                print("No valid contacts entered. Please try again.")
                continue

            message = input("Enter message text (max 390 chars): ")
            if not message:
                print("Message text cannot be empty. Please try again.")
                continue
            if len(message) > 390:
                print(f"Message too long ({len(message)} chars). Max is 390. Please shorten your message.")
                continue

            # Call send_sms without masking parameters as per your request
            send_response = send_sms(contacts, message)
            print("\n--- SMS Send API Response ---")
            print(json.dumps(send_response, indent=4))
            if send_response.get("success"):
                print("\nSMS sending process initiated successfully!")
                for item in send_response.get("data", []):
                    print(f"  Contact: {item.get('contact')}, Status: {item.get('status')}, Message: {item.get('message')}, Track ID: {item.get('track_id')}")
            else:
                print("\nFailed to initiate SMS sending.")
                print(f"Error Message: {send_response.get('message', 'No specific error message.')}")

        elif choice == '2':
            track_id = input("Enter the Track ID of the SMS to query: ").strip()
            if not track_id:
                print("Track ID cannot be empty. Please try again.")
                continue

            track_response = track_sms(track_id)
            print("\n--- SMS Track API Response ---")
            print(json.dumps(track_response, indent=4))
            if track_response.get("success"):
                print("\nSMS tracking successful!")
                data = track_response.get("data", {})
                print(f"  Track ID: {data.get('track_id')}")
                print(f"  Contact: {data.get('contact')}")
                print(f"  Sender: {data.get('sender')}")
                print(f"  Text: {data.get('text')}")
                print(f"  Cost: {data.get('cost')}")
                print(f"  Is Masking: {'Yes' if data.get('is_masking') == 1 else 'No'}")
                print(f"  Status: {data.get('status')}")
            else:
                print("\nFailed to track SMS.")
                print(f"Error Message: {track_response.get('message', 'No specific error message.')}")

        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# --- Main execution block ---
if __name__ == "__main__":
    main_menu()

