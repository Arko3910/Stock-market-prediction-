from huggingface_hub import HfApi
api = HfApi()
api.create_repo(
    repo_id="DataSynthis_ML_JobTask",
    repo_type="space",
    space_sdk="gradio"
)