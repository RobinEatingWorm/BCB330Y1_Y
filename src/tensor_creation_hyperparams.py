class Hyperparams:
    """
    Contains hyperparameters for a specific image used in creating the data
    tensor.

    === Attributes ===

    name:
        The main name of the data.
    estimates:
        A list of paths to the preprocessed CNMF data.
    trial:
        A path to the trial metadata.
    trial_var:
        The variable name within the trial metadata containing the metadata.
    trial_time_field:
        The name of the field containing time information in the trial
        metadata.
    trial_output_field:
        The name of the field containing output information in the trial
        metadata.
    trial_fr:
        The frame rate of the recorded trial information.
    image:
        A path to the image metadata.
    image_var:
        The variable name within the image metadata containing the metadata.
    image_time_field:
        The name of the field containing time information in the image
        metadata.
    image_fr:
        The frame rate of imaging.
    snr_thr:
        The SNR threshold. Components with a SNR lower than this threshold
        will be removed.
    baseline_name:
        Trials with this string in their output field are considered
        baselines.
    baseline_selected:
        The index determining which baseline to use for classifying noise
        regions.
    n_clusters:
        The number of clusters used for hierarchical clustering of
        components.
    heatmap_bound:
        The number of standard deviations used to anchor the colormap of
        heatmaps showing z-scored data.
    events_field:
        Names of fields in the trial metadata containing frames when certain
        alignment events occurred.
    align_opts:
        A list of options for aligning intervals between events.
    """

    # Main name of the data
    name: str

    # Preprocessed data
    estimates: list[str]

    # Trial metadata
    trial: str
    trial_var: str
    trial_time_field: str
    trial_output_field: str
    trial_fr: float

    # Image metadata
    image: str
    image_var: str
    image_time_field: str
    image_fr: float

    # Component evaluation
    snr_thr: float
    baseline_name: str
    baseline_selected: int

    # Visualization
    n_clusters: int
    heatmap_bound: int

    # Alignment
    events_field: list[str]
    align_opts: list[tuple]

    def __init__(self, name: str) -> None:
        """
        Initialize a new Hyperparams object with the given name.
        :param name: The main name of the data.
        """

        self.name = name
        self.estimates = []
        self.trial = ''
        self.trial_var = ''
        self.trial_time_field = ''
        self.trial_output_field = ''
        self.trial_fr = 0.0
        self.image = ''
        self.image_var = ''
        self.image_time_field = ''
        self.image_fr = 0.0
        self.snr_thr = 0.0
        self.baseline_name = ''
        self.baseline_selected = 0
        self.n_clusters = 0
        self.heatmap_bound = 0
        self.events_field = []
        self.align_opts = []

    def set_data_paths(self, estimates: list[str]) -> None:
        """
        Set the paths to all estimates containing preprocessed data for the
        image.
        :param estimates: A list of paths to .hdf5 files with preprocessed data.
        """

        self.estimates = estimates

    def set_trial_metadata(self, trial: str, trial_var: str, trial_time_field: str, trial_output_field: str,
                           trial_fr: float) -> None:
        """
        Set trial metadata information.
        :param trial: A path to a MAT-file with trial metadata.
        :param trial_var: The variable name within the trial metadata containing
            the metadata.
        :param trial_time_field: The name of the field with time information.
        :param trial_output_field: The name of the field with output information.
        :param trial_fr: The frame rate of the recorded trial information.
        """

        self.trial = trial
        self.trial_var = trial_var
        self.trial_time_field = trial_time_field
        self.trial_output_field = trial_output_field
        self.trial_fr = trial_fr

    def set_image_metadata(self, image: str, image_var: str, image_time_field: str, image_fr: float) -> None:
        """
        Set image metadata information.
        :param image: A path to a MAT-file with image metadata.
        :param image_var: The variable name within the image metadata containing
            metadata.
        :param image_time_field: The name of the field with time information.
        :param image_fr: The frame rate of imaging.
        """

        self.image = image
        self.image_var = image_var
        self.image_time_field = image_time_field
        self.image_fr = image_fr

    def set_component_evaluation(self, snr_thr: float, baseline_name: str, baseline_selected: int) -> None:
        """
        Set the parameters for manually evaluating components.
        :param snr_thr: The SNR threshold.
        :param baseline_name: If a trial has a string that matches this in its
            output field, it is considered a baseline.
        :param baseline_selected: The index determining which baseline to
            use for classifying noise regions.
        """

        self.snr_thr = snr_thr
        self.baseline_name = baseline_name
        self.baseline_selected = baseline_selected

    def set_visualization_params(self, n_clusters: int, heatmap_bound: int) -> None:
        """
        Set the parameters used for visualizing components.
        :param n_clusters: The number of clusters to use for hierarchical
            clustering of components.
        :param heatmap_bound: The number of standard deviations used to anchor
            the colormaps of heatmaps showing z-scored data.
        """

        self.n_clusters = n_clusters
        self.heatmap_bound = heatmap_bound

    def set_alignment_params(self, events_field: list[str], align_opts: list[tuple]) -> None:
        """
        Set parameters for aligning neuronal time series. Here are the
        currently supported alignment options in tuple form:
         * ('interpolate', X) --- Interpolate X frames into the interval if
           X is an integer. X can also be set to 'mean', in which case the mean
           number of frames across all trials will be the number of frames
           interpolated.
         * ('stitch', [X, Y]) --- Concatenate the first X frames and last Y
           frames within the interval together, ignoring all frames in the
           middle. X and Y are both integers.
         * ('truncate', X) --- If X is set to 'min', truncate each interval to
           have as many frames as the trial with the least number of frames in
           the interval. If X is set to an integer AND the number of frames in
           the trial with the least frames is greater than X, truncate each
           interval to have X frames.
        Undefined behavior will occur if other tuples that do not match the
        ones aforementioned are used.
        :param events_field: A list of variable names within the trial metadata
            with event frame information. The events must be chronologically
            ordered and, along with the start and end of the data, will divide the
            data into intervals used for time series alignment.
        :param align_opts: A list of tuples containing alignment options used
            for each interval. The number of elements in this list must be one
            greater than the number of events and correspond to chronologically
            ordered intervals separated by the events.
        """

        # Raise an error if an invalid amount of events or options are passed
        if len(events_field) + 1 != len(align_opts):
            raise ValueError("The number of alignment options must be one " +
                             "greater than the number of events.")

        self.events_field = events_field
        self.align_opts = align_opts
