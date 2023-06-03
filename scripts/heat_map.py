from caiman.source_extraction.cnmf import cnmf

import matplotlib.pyplot as plt
import os
import seaborn as sns

from src.array import normalize


def main() -> None:
    """
    Plot a heat map of the normalized neuronal activity traces.
    """

    # Move to the parent directory of the results folder
    os.chdir('C:/Users/pugavin/BCB-330-2023-05/pugavin/')

    # List of saved CNMF data files
    fnames = ['results/F147_memmap__d1_320_d2_256_d3_1_order_C_frames_41990_.hdf5',
              'results/F201_memmap__d1_320_d2_256_d3_1_order_C_frames_48080_.hdf5']

    # Plot data from each file
    for fname in fnames:

        # Load and normalize the neuronal activity traces
        cnm = cnmf.load_CNMF(fname)
        data = normalize(cnm.estimates.S, 1)

        # Create a heatmap
        sns.set_theme(rc={'figure.figsize': (17, 8.5)})
        sns.heatmap(data, cmap='jet')
        plt.show(block=True)


if __name__ == '__main__':
    main()
