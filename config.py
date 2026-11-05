import os
from dotenv import load_dotenv

load_dotenv()

# n8n Workflow URLs
WORKFLOW_A = os.getenv("WORKFLOW_A")
WORKFLOW_B = os.getenv("WORKFLOW_B")

# Connection Settings
TIMEOUT = 90
MAX_RETRIES = 3

# Display Labels
CARPARK_TYPE_LABELS = {
    "SURFACE CAR PARK":        "Surface",
    "MULTI-STOREY CAR PARK":   "Multi-storey",
    "BASEMENT CAR PARK":       "Basement",
    "COVERED CAR PARK":        "Covered",
    "MECHANISED CAR PARK":     "Mechanised"
}

PARKING_SYSTEM_LABELS = {
    "ELECTRONIC PARKING":      "Electronic",
    "COUPON PARKING":          "Coupon"
}

# Menu Options
TYPE_OPTIONS = {
    1: "SURFACE CAR PARK",
    2: "MULTI-STOREY CAR PARK",
    3: "BASEMENT CAR PARK",
    4: "COVERED CAR PARK",
    5: "MECHANISED CAR PARK",
    6: None
}

SYSTEM_OPTIONS = {
    1: "ELECTRONIC PARKING",
    2: "COUPON PARKING",
    3: None
}
