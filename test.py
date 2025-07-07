import requests
import base64

# 1. Fill these in
HOST      = "https://<your-databricks-workspace>"  # e.g. https://adb-123456789012345.18.azuredatabricks.net
TOKEN     = "dapiXXXXXXXXXXXXXXXXXXXXXXXXXXXX"    # your Databricks API token
DBFS_PATH = "/path/to/your/file.txt"               # the DBFS filepath you want to read
LOCAL_OUT = "file.txt"                             # where to save it locally

# 2. Prepare headers
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

# 3. Read the file from DBFS
resp = requests.get(
    f"{HOST}/api/2.0/dbfs/read",
    headers=headers,
    json={"path": DBFS_PATH, "offset": 0, "length": -1}
)
resp.raise_for_status()

# 4. Decode the base64-encoded data and write it out
data_b64 = resp.json().get("data", "")
with open(LOCAL_OUT, "wb") as f:
    f.write(base64.b64decode(data_b64))

print(f"Downloaded DBFS file {DBFS_PATH} → ./{LOCAL_OUT}")
