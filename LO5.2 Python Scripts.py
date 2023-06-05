# Basic Python working


print("strings can be printed like this")

vars = "this is a variable"

print(vars)

type(vars)


# Use Pandas package
# Python packages should be installed isolated in a Python environment
# See associated r script

import pandas as pd




# Create a data frame

dat = pd.DataFrame(
  {
    "Name": [
      "Ellie",
      "Joel",
      "Tess"
      ],
      "Age": [3, 7, 6],
      "Spp": ["cat", "dog", "dog"],
  }
)

dat


dat["Age"]





dat["Age"].max()




dat.describe()

dat.head()

dat.dtypes







# Subsetting data

ages = dat["Age"]

ages



type(dat["Age"])
dat["Age"].shape


age_spp = dat[["Age", "Spp"]]
age_spp.head()



above_3 = dat[dat["Age"] > 3]
above_3.head()

