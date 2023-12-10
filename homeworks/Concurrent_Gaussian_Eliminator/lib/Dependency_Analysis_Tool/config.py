class Config:
    def __init__(
        self,
        alphabet: list[str],
        raw_trace: str,
        raw_transactions: dict[str, str],
        output_directory_path:str,
        labels_with_indices:bool
        ):
        self.alphabet = alphabet
        self.raw_trace = raw_trace
        self.raw_transactions = raw_transactions
        self.output_directory_path = output_directory_path
        self.labels_with_indices = labels_with_indices
