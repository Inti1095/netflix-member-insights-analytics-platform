import json
import random
import uuid
from datetime import datetime

EVENT_TYPES = ["play", "pause", "search", "recommendation_click"]

def generate_event():
    return {
        "user_id": str(uuid.uuid4()),
        "event_type": random.choice(EVENT_TYPES),
        "content_id": random.randint(1, 1000),
        "watch_time": random.randint(0, 5000),
        "timestamp": datetime.utcnow().isoformat()
    }

def generate_events(n=100000):
    with open("data/raw/events.json", "w") as f:
        for _ in range(n):
            json.dump(generate_event(), f)
            f.write("\n")

if __name__ == "__main__":
    generate_events(1000000)
