import pandas as pd
import matplotlib.pyplot as plt
import os

from dotenv import load_dotenv

load_dotenv()

CSV= os.getenv('CSV_FILE')

DF = pd.read_csv(CSV)






