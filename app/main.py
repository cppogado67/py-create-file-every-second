from datetime import datetime
import time
while True:
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    filename = f"app-{now.hour}_{now.minute}_{now.second}.log"
    
    with open(filename, "w") as f:
        f.write(timestamp)
    
    print(f"{timestamp} {filename}")
    time.sleep(1)
