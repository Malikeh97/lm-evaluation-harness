import datasets
def process_docs(dataset: datasets.Dataset) -> datasets.Dataset:
    def _process_doc(doc):
        out_doc = {
            "query": doc["inputs"],
            "choices": doc["multiple_choice_targets"],
            "gold": doc["answer"],
        }
        return out_doc

    return dataset.map(_process_doc)