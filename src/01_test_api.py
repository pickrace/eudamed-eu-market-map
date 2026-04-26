"""
EUDAMED API - Test Connection
First contact with the EUDAMED public API.
Fetches a small sample of medical device data and saves the raw response.
"""

import requests
import json
from pathlib import Path

# === CONFIGURATION ===
BASE_URL = "https://ec.europa.eu/tools/eudamed/api/devices/udiDiData"
PARAMS = {
    "page": 0,
    "pageSize": 25,
    "deviceStatusCode": "refdata.device-model-status.on-the-market",
    "languageIso2Code": "en",
    "sort": "lastUpdateDate,desc"
}
HEADERS = {
    "Accept": "application/json",
    "User-Agent": "EUDAMED-Research-Project/1.0"
}
OUTPUT_FILE = Path("data/raw/test_response.json")


def main():
    # --- Make the request ---
    print("Connecting to EUDAMED API...")
    print(f"URL: {BASE_URL}")

    response = requests.get(BASE_URL, params=PARAMS, headers=HEADERS, timeout=30)

    # --- Check if request was successful ---
    print(f"Status code: {response.status_code}")

    if response.status_code != 200:
        print(f"ERROR: Expected 200, got {response.status_code}")
        print(f"Response: {response.text[:500]}")
        return

    print("Connection successful!")

    # --- Parse JSON response ---
    data = response.json()

    print(f"Total devices in EUDAMED: {data.get('totalElements', 'N/A')}")
    print(f"Total pages of results: {data.get('totalPages', 'N/A')}")
    print(f"Devices in this response: {len(data.get('content', []))}")

    if data.get("content"):
        first_device = data["content"][0]
        print("\n--- First device details ---")
        print(f"Trade name: {first_device.get('tradeName', 'N/A')}")
        print(f"Manufacturer: {first_device.get('manufacturerName', 'N/A')}")

        risk_class_obj = first_device.get("riskClass")
        if risk_class_obj:
            risk_code = risk_class_obj.get("code", "N/A")
        else:
            risk_code = "N/A"
        print(f"Risk class: {risk_code}")

        srn = first_device.get("manufacturerSrn")
        if srn:
            country = srn.split("-")[0]  # split SRN by "-" and take first element
        else:
            country = "N/A"
        print(f"Country (from manufacturer SRN): {country}")

    print("\n--- Top-level keys in response ---")
    for key in data.keys():
        print(f"  {key}: {type(data[key]).__name__}")

    print(f"\nSaving raw response to {OUTPUT_FILE}...")
    with OUTPUT_FILE.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()