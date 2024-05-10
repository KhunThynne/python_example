import os
from dotenv import load_dotenv

load_dotenv()


Test = os.getenv('Test')
print(Test)