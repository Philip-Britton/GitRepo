import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas as pd
import seaborn as sns
df = pd.read_csv("updated_listings5.csv")
sns.catplot(x="region_parent_name", kind="count", data=df)
plt.xticks(rotation=90)
plt.show()




