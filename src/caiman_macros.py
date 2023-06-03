import caiman as cm
from caiman.cluster import setup_cluster
from caiman.source_extraction.cnmf import cnmf, params

from multiprocessing import Pool
from typing import List, Optional, Tuple


def resave_data(data: List[str], dest: List[str]) -> None:
    """
    Load TIFF data and save it to another directory.
    :param data: A list containing paths to the data.
    :param dest: A list containing paths to where the data should be resaved.
    """

    # Check that function inputs are correct
    if len(data) != len(dest):
        raise IndexError("The number of data sources and destinations must be \
                         the same.")

    # Load the data and then save it
    for i in range(len(data)):
        cm.load(data[i]).save(dest[i])


def start_cluster(dview: Optional[Pool] = None) -> Tuple[Pool, int]:
    """
    Start (or restart) a local cluster to enable parallel processing.
    :param dview: A Pool object.
    :returns: A tuple containing a Pool object and an int with the approximate
    number of machine cores minus 1.
    """

    # Stop the current multiprocessing pool if one is active
    if dview is not None:
        cm.stop_server(dview=dview)

    # Start the cluster
    return setup_cluster()[1:3]


def run_pipeline(n_processes: int, params_dict: dict,
                 dview: Pool) -> cnmf.CNMF:
    """
    Run the main CaImAn pipeline on a file.
    :param n_processes: The approximate number of machine cores minus 1.
    :param params_dict: A dictionary of parameters for CNMF.
    :param dview: A Pool object.
    :return: A cnmf.CNMF object.
    """

    # Run the CaImAn pipeline
    cnmf_params = params.CNMFParams(params_dict=params_dict)
    cnm = cnmf.CNMF(n_processes=n_processes, params=cnmf_params, dview=dview)
    return cnm.fit_file(motion_correct=True, include_eval=True)
