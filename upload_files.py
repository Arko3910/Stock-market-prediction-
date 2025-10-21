from huggingface_hub import HfApi
api = HfApi()

api.upload_file(
    path_or_fileobj="D:/Arko/Data sythesis project/app.py",
    path_in_repo="app.py",
    repo_id="Arko3910/DataSynthisMLJobTask",
    repo_type="space",
)

api.upload_file(
    path_or_fileobj="D:/Arko/Data sythesis project/samsung_stock.csv",
    path_in_repo="samsung_stock.csv",
    repo_id="Arko3910/DataSynthisMLJobTask",
    repo_type="space",
)