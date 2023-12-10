# INPUT_DIRECTORY_PATH = "inputs/"
# OUTPUT_DIRECTORY_PATH = "outputs/"
# PRINT_FNF = True
# PRINT_PLOT = True
# EXPORT_PLOT_TO_PNG = True
# EXPORT_GRAPH_TO_DOT = True
# LABELS_WITH_INDICES = False

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
    
