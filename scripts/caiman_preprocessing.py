import os

import src.caiman_macros as cm_macros


def resave_data_path() -> None:
    """
    Wrapper used for calling cm_macros.resave_data on the specified file paths.
    """

    # Move to the parent directory of the data and results folders
    os.chdir('C:/Users/pugavin/BCB-330-2023-05/pugavin/')

    # Call cm_macros.resave_data on the specified file paths
    data = ['data/2p_raw/F147/F147_20210526_fish4_blk1_LT_9dpf_00001.tif',
            'data/2p_raw/F201/F201_20210812_fish2_blk1_RT_9dpf_00001.tif']
    fnames = ['results/F147.tif', 'results/F201.tif']
    cm_macros.resave_data(data, fnames)


def get_params_dict() -> dict:
    """
    Returns parameter needed for CaImAn.
    :return: A dictionary of parameters.
    """

    # Parameter dictionary for CNMFParams
    params_dict = {
        'gSig': [3, 3],    # Half size of neurons (tau)
        'merge_thr': 0.5,  # Threshold for merging
        'min_SNR': 2.5,    # Trace SNR threshold
        'rval_thr': 0.6,   # Space correlation threshold
        'p': 2,            # Order of AR model
        'pw_rigid': True,  # Perform rigid motion correction
        'use_cuda': True   # Use a GPU
    }
    return params_dict


def preprocess_condensed(params_dict: dict) -> None:
    """
    Preprocess the data using macros with the fit_file function.
    Note that components are NOT selected using this method.
    :param params_dict: A dictionary of parameters.
    """

    # Start a cluster
    dview, n_processes = cm_macros.start_cluster()

    # Run the CaImAn pipeline
    cm_macros.run_pipeline(n_processes, params_dict, dview)


def main() -> None:
    """
    Preprocess the data using CaImAn.
    """

    # Load and resave the data
    # See GitHub Issue #377 - https://github.com/flatironinstitute/CaImAn/issues/377#issuecomment-426740429
    # resave_data_path()

    # Get the paths to the data
    os.chdir('C:/Users/pugavin/BCB-330-2023-05/pugavin/results')
    fnames = ['F147.tif', 'F201.tif']

    # Retrieve parameters
    params_dict = get_params_dict()

    # Analyze all files
    for fname in fnames:

        # Add the file to the parameter dictionary
        params_dict['fnames'] = [fname]

        # Begin preprocessing
        preprocess_condensed(params_dict)


if __name__ == '__main__':
    main()
