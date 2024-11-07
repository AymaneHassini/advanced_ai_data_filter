from transformers import AutoModelForSequenceClassification, AutoTokenizer
from transformers import Trainer

checkpoint = "./checkpoint-30"


def load_classifier():
    # Preparing the model
    classifier = AutoModelForSequenceClassification.from_pretrained(
        checkpoint, num_labels=5
    )
    tokenizer = AutoTokenizer.from_pretrained(checkpoint)
    trainer = Trainer(
        classifier,
    )

    return trainer, tokenizer
