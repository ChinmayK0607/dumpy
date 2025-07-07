from databricks.sdk import WorkspaceClient

# 1. Fill these in
HOST      = "https://<your-databricks-workspace>"  # e.g. https://adb-123456789012345.18.azuredatabricks.net
TOKEN     = "dapiXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
DBFS_PATH = "/path/to/your/file.txt"
LOCAL_OUT = "file.txt"

# 2. Initialize the client
client = WorkspaceClient(host=HOST, token=TOKEN)

# 3. Fetch the file
resp = client.dbfs.get(path=DBFS_PATH)

# 4. Write it locally
with open(LOCAL_OUT, "wb") as f:
    f.write(resp.data)

print(f"Downloaded DBFS file {DBFS_PATH} → {LOCAL_OUT}")
