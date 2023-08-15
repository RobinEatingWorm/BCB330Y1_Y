class Hyperparams:
    """
    Contains hyperparameters for decompositions (dPCA and TCA).

    === Attributes ===

    name:
        The main name of the data.
    path:
        A path to the data array.
    n_components:
        The number(s) of components to find.
    rep:
        The number of models to fit for each number of components.
    methods:
        A tuple of decomposition methods to use (for TCA).
    events_name:
        Names of events used for alignment.
    events_time:
        The indices where events occurred.
    """

    # Name and location
    name: str
    path: str

    # Decomposition
    n_components: range
    rep: int

    # TCA-specific methods
    methods: list[str]

    # Events
    events_name: list[str]
    events_time: list[int]

    def __init__(self, name: str) -> None:
        """
        Initialize a new Hyperparams object with the given name.
        :param name: The main name of the data.
        """

        self.name = name
        self.path = ''
        self.n_components = range(0, 0)
        self.rep = 0
        self.methods = []
        self.events_name = []
        self.events_time = []

    def set_path(self, path: str) -> None:
        """
        Set the path to the data.
        :param path: The path to the data.
        """

        self.path = path

    def set_decomp_params(self, n_components: range, rep: int) -> None:
        """
        Set general parameters for performing decompositions.
        :param n_components: The number of components to decompose the data
            into. This can be a single integer or a range of integers.
        :param rep: The number of times to perform decompositions for each
            distinct number of components.
        """

        self.n_components = n_components
        self.rep = rep

    def set_decomp_methods(self, methods: list[str]) -> None:
        """
        Set the decomposition methods used (TCA only).
        :param methods: A list of decomposition methods.
        """

        self.methods = methods

    def set_events(self, events_name: list[str], events_time: list[int]) -> None:
        """
        Set the names and times of alignment events.
        :param events_name: Names of events.
        :param events_time: Times (frames) when events occurred.
        """

        self.events_name = events_name
        self.events_time = events_time
