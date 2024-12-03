from urllib.parse import quote_plus

# Replace these values with your actual username and password
db_username = "mridulg"
db_password = "admin123"

# Encode the credentials
encoded_username = quote_plus(db_username)
encoded_password = quote_plus(db_password)

# Construct the URI
MONGO_URI = (
    f"mongodb+srv://{encoded_username}:{encoded_password}"
    f"@cosmocloudtask.gkbif.mongodb.net/"
    f"?retryWrites=true&w=majority&appName=CosmoCloudtask"
)

print("MongoDB URI:", MONGO_URI)
