import kagglehub

# Download latest version
path = kagglehub.dataset_download("swetashetye/lending-club-loan-data-imbalance-dataset")

print("Path to dataset files:", path)