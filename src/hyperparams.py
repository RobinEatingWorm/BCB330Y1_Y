class Hyperparams:
    """
    Contains hyperparameters for a specific image used for CaImAn and other
    preprocessing steps.

    === Attributes ===

    name:
        The main name of the data.
    path_orig:
        The path to the data's original location.
    path_src:
        The path to the data's primary location. Use this path to access
        the data.
    params_dict:
        A dictionary of parameters used by CaImAn.
    local_max_thr:
        The threshold for determining which mean fluorescence values may be
        local maxima.
    local_max_rad:
        The number of points to check around a potential local maximum.
    channel_thr:
        The threshold to separate different color channels.
    correction_thr:
        The threshold for determining which pixel rows must be replaced.
    correction_rad:
        The number of frames around a local maximum to check pixel rows.
    lr_proxy:
        Whether to perform line removal by proxy.
    proxy_slices:
        A list of rectangular slices of the image data to set to np.nan.
    piecewise_proc:
        Whether to run CNMF on a subrectangle of the entire area.
    proc_slices:
        A list of possible subrectangles.
    proc_index:
        An index into proc_slices specifying which subrectangle to run
        CNMF on.
    """

    # Main name of the data
    name: str

    # File locations
    path_orig: str
    path_src: str

    # CaImAn parameters
    params_dict: dict

    # Line removal
    local_max_thr: int
    local_max_rad: int
    channel_thr: int
    correction_thr: int
    correction_rad: int

    # Line removal by proxy
    lr_proxy: bool
    proxy_slices: list[tuple[slice, slice]]

    # Piecewise processing
    piecewise_proc: bool
    proc_slices: list[tuple[slice, slice]]
    proc_index: int

    def __init__(self, name: str) -> None:
        """
        Initialize a new Hyperparams object with the given name.
        :param name: The main name of the data.
        """

        self.name = name
        self.path_orig = ''
        self.path_src = ''
        self.params_dict = {}
        self.local_max_thr = 0
        self.local_max_rad = 0
        self.channel_thr = 0
        self.correction_thr = 0
        self.correction_rad = 0
        self.lr_proxy = False
        self.proxy_slices = []
        self.piecewise_proc = False
        self.proc_slices = []
        self.proc_index = 0

    def set_paths(self, path_orig: str, path_src: str) -> None:
        """
        Set the original and source paths of the data.
        :param path_orig: The path to the data's original location.
        :param path_src: The path to the data's primary location.
        """

        self.path_orig = path_orig
        self.path_src = path_src

    def set_params_dict(self, tau: int) -> None:
        """
        Set parameters defined by CaImAn.
        :param tau: Half size of neurons.
        """

        self.params_dict = {
            'gSig': [tau, tau],              # Half size of neurons (tau)
            'merge_thr': 0.5,                # Threshold for merging
            'min_SNR': 2.5,                  # Trace SNR threshold
            'rval_thr': 0.6,                 # Space correlation threshold
            'p': 2,                          # Order of AR model
            'use_cuda': True                 # Use a GPU
        }

    def set_fname(self, fname: str) -> None:
        """
        Set the file path in the parameter dictionary.
        :param fname: The path of the data file.
        """

        self.params_dict['fnames'] = [fname]

    def set_lr_params(self, local_max_thr: int, local_max_rad: int, channel_thr: int,
                      correction_thr: int, correction_rad: int) -> None:
        """
        Set parameters for line removal.
        :param local_max_thr: The threshold for which local maxima must be above.
        :param local_max_rad: The radius around a potential local maximum to check.
        :param channel_thr: The threshold to separate different color channels.
        :param correction_thr: The threshold for determining which pixel rows must be
        replaced.
        :param correction_rad: The radius around a local maximum to replace pixel rows.
        """

        self.local_max_thr = local_max_thr
        self.local_max_rad = local_max_rad
        self.channel_thr = channel_thr
        self.correction_thr = correction_thr
        self.correction_rad = correction_rad

    def set_lr_proxy_params(self, proxy_slices: list[tuple[slice, slice]]) -> None:
        """
        Set parameters for line removal by proxy.
        :param proxy_slices: A list of rectangular slices of the image data to
        set to np.nan.
        """

        self.lr_proxy = True
        self.proxy_slices = proxy_slices

    def set_piecewise_processing(self, proc_slices: list[tuple[slice, slice]]) -> None:
        """
        Set parameters for piecewise processing except for proc_index, which
        can be set manually.
        :param proc_slices: A list of rectangular slices of the image data.
        """

        self.piecewise_proc = True
        self.proc_slices = proc_slices
