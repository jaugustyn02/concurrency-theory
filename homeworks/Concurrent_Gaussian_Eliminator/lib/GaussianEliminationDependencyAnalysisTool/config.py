class Config:
    def __init__(
            self,
            OUTPUT_DIRECTORY_PATH="outputs/",
            PRINT_FNF=False,
            SAVE_FNF=True,
            PRINT_PLOT=True,
            EXPORT_PLOT_TO_PNG=True,
            EXPORT_GRAPH_TO_DOT=True,
            LABELS_WITH_INDICES=False
        ):
        self.OUTPUT_DIRECTORY_PATH = OUTPUT_DIRECTORY_PATH
        self.PRINT_FNF = PRINT_FNF
        self.SAVE_FNF = SAVE_FNF
        self.PRINT_PLOT = PRINT_PLOT
        self.EXPORT_PLOT_TO_PNG = EXPORT_PLOT_TO_PNG
        self.EXPORT_GRAPH_TO_DOT = EXPORT_GRAPH_TO_DOT
        self.LABELS_WITH_INDICES = LABELS_WITH_INDICES
