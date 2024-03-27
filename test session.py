from dotenv import load_dotenv
import os
from supabase import create_client

load_dotenv()

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)


# data = supabase.auth.sign_in_with_oauth({
#   "provider": 'facebook'})

datas = supabase.table("players").select()