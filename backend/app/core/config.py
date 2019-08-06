import os


# $ cd env
# $ source bin/activate
# load_dotenv(".env")

API_V1 = "/api"

SECRET_KEY = os.getenvb(b"SECRET_KEY")
if not SECRET_KEY:
    SECRET_KEY = os.urandom(32)


ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 8  # 60 minutes * 24 hours * 8 days = 8 days

PROJECT_NAME = os.getenv("PROJECT_NAME", "Notification application")



