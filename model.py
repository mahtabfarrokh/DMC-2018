import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


new_data = pd.read_csv("new_data.csv")
plt.plot(new_data["Log_Date"], new_data["COUNT"])
plt.show()

