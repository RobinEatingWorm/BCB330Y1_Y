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
    trial_heat_onset_field:
        The name of the field containing information on when the heat source
        was turned on in each trial.
    trial_turn_field:
        The name of the field containing information on when the fish turned
        in each trial.
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
    max_seconds_turn_to_end:
        The maximum number of seconds to keep starting from when the fish first
        turned to the end of the trial.
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
    trial_heat_onset_field: str
    trial_turn_field: str
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

    # Alignment parameters
    max_seconds_turn_to_end: int

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
        self.trial_heat_onset_field = ''
        self.trial_turn_field = ''
        self.trial_fr = 0.0
        self.image = ''
        self.image_var = ''
        self.image_time_field = ''
        self.image_fr = 0.0
        self.snr_thr = 0.0
        self.baseline_name = ''
        self.baseline_selected = 0
        self.max_seconds_turn_to_end = 0

    def set_data_paths(self, estimates: list[str]) -> None:
        """
        Set the paths to all estimates containing preprocessed data for the
        image.
        :param estimates: A list of paths to .hdf5 files with preprocessed data.
        """

        self.estimates = estimates

    def set_trial_metadata(self, trial: str, trial_var: str, trial_time_field: str, trial_output_field: str,
                           trial_heat_onset_field: str, trial_turn_field: str, trial_fr: float) -> None:
        """
        Set trial metadata information.
        :param trial: A path to a MAT-file with trial metadata.
        :param trial_var: The variable name within the trial metadata containing
        the metadata.
        :param trial_time_field: The name of the field with time information.
        :param trial_output_field: The name of the field with output information.
        :param trial_heat_onset_field: The name of the field with information on
        when the heat source was turned on.
        :param trial_turn_field: THe name of the field with information on when
        the fish turned.
        :param trial_fr: The frame rate of the recorded trial information.
        """

        self.trial = trial
        self.trial_var = trial_var
        self.trial_time_field = trial_time_field
        self.trial_output_field = trial_output_field
        self.trial_heat_onset_field = trial_heat_onset_field
        self.trial_turn_field = trial_turn_field
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

    def set_alignment_params(self, max_seconds_turn_to_end) -> None:
        """
        Set parameters for aligning neuronal time series.
        :param max_seconds_turn_to_end: The maximum number of seconds to keep
        from when the fish first turned to the end of the trial.
        """

        self.max_seconds_turn_to_end = max_seconds_turn_to_end
