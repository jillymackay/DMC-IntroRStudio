
# Creating and running a conda environment for python through r studio
# You need to run this if you want R Studio to talk Pythonese

library(reticulate)
conda_create("r-reticulate")

# Installing packages

conda_install(envname = "r-reticulate",
              packages = c("pandas"))






