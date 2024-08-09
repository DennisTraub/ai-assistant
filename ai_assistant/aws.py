import boto3


def list_profiles():
    profiles = boto3.Session().available_profiles
    if not profiles or len(profiles) == 0:
        return "No AWS profiles found", None
        
    return "Available AWS profiles:", profiles

def list_models(all: bool, provider: str):
    bedrock = boto3.client("bedrock")
    params = {}
    if not all:
        params["byInferenceType"] = "ON_DEMAND"
    if provider:
        params["byProvider"] = provider
    
    models = bedrock.list_foundation_models(**params)["modelSummaries"]
    return models