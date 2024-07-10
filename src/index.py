import ray
from datasets import load_dataset


from src.data_insert_retrieve import StoreResults

def set_index(embedding_model_name, insert_dataset=True, contexts=None):
    if insert_dataset:
        data = load_dataset("squad", split="train[:200]")
        ray_ds = ray.data.from_huggingface(data)
    else:
        ray_ds = ray.data.from_items([
            {'context': context} for context in contexts
            ])

    