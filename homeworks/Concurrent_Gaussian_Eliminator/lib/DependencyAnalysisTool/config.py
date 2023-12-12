class Config:
    def __init__(
            self,
            OUTPUT_DIRECTORY_PATH:str="OUTPUTS/",
            PRINT_FNF:bool=False,
            SAVE_FNF:bool=False,
            PRINT_PLOT:bool=False,
            EXPORT_PLOT_TO_PNG:bool=False,
            EXPORT_GRAPH_TO_DOT:bool=False,
            LABELS_WITH_INDICES:bool=False
        ):
        self.OUTPUT_DIRECTORY_PATH = OUTPUT_DIRECTORY_PATH
        self.PRINT_FNF = PRINT_FNF
        self.SAVE_FNF = SAVE_FNF
        self.PRINT_PLOT = PRINT_PLOT
        self.EXPORT_PLOT_TO_PNG = EXPORT_PLOT_TO_PNG
        self.EXPORT_GRAPH_TO_DOT = EXPORT_GRAPH_TO_DOT
        self.LABELS_WITH_INDICES = LABELS_WITH_INDICES

