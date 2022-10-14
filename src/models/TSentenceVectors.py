# model packages
import torch
import torch.nn as nn
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModel

from src.utils.preprocess import preprocess_text

# Mean Pooling - Take attention mask into account for correct averaging
def mean_pooling(model_output, attention_mask):
    token_embeds = model_output[0] #First element of model_output contains all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeds.size()).float()
    return torch.sum(token_embeds * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)


class TSentenceVectors(nn.Module):
    def __init__(self, model_id: str = "sentence-transformers/all-MiniLM-L6-v2"):
        super(TSentenceVectors, self).__init__()

        self.model = AutoModel.from_pretrained(model_id)
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)

    def forward(self, text: str, split = "\n\n+"):
        sentences = preprocess_text(text, split)
        encoded_input = self.tokenizer(sentences, padding=True, truncation=True, return_tensors="pt")

        with torch.no_grad():
            model_output = self.model(**encoded_input)

        embeddings = mean_pooling(model_output, encoded_input["attention_mask"])
        embeddings = F.normalize(embeddings, p=2, dim=1)
        return embeddings




