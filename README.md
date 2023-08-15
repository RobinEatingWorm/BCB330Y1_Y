# Experience-Dependent Latent Variables in Neuronal Populations

## Installation

### General

Download or clone this repository from GitHub.
In the main project folder (containing this README), run the following commands to create and activate a new conda environment named `BCB330Y1_Y`.
This name can be changed to anything else.

```sh
conda create -n BCB330Y1_Y
conda activate BCB330Y1_Y
```

Next, install [mamba](https://mamba.readthedocs.io/en/latest/).
This will speed up later installation of Python packages.

```sh
conda install -c conda-forge mamba
```

Move to the main project folder and install the required packages from [`environment.yml`](environment.yml).

```sh
mamba env update -n BCB330Y1_Y -f environment.yml
```

Finally, install the [`src`](src) package within this project.

```sh
pip install -e .
```

### Lin Lab GPU

Alternatively, if you are using the GPU in the Lin Lab, there is a method of installation that avoids problems with filename length when installing TensorFlow.
In the main project folder (containing this README), run the following conda commands to clone the existing `tf-gpu` environment into a new one named `BCB330Y1_Y`.
This name can be changed to anything else.

```sh
conda create -n BCB330Y1_Y --clone tf-gpu
conda activate BCB330Y1_Y
```

The rest of the commands are almost the same as the ones used in the previous section.
The key difference is to use [`environment_lin_lab_gpu.yml`](environment_lin_lab_gpu.yml) to install packages with mamba.

```sh
conda install -c conda-forge mamba
mamba env update -n BCB330Y1_Y -f environment_lin_lab_gpu.yml
pip install -e .
```

## Directories and Files

This project uses the following directories and files.

* `data` - Not included in the repository.
  All raw data used in analyses should be placed in here.
* `results` - Not included in the repository.
  The results of all analyses should be automatically placed in here.
* [`scripts`](scripts) - Contains all Jupyter Notebook files.
  These files constitute the main analysis pipeline.
  * [`caiman_preprocessing.ipynb`](scripts/caiman_preprocessing.ipynb) - Preprocessing steps for neuroimaging data and code to run [CaImAn](https://github.com/flatironinstitute/CaImAn) for motion correction and source extraction.
  * [`dPCA.ipynb`](scripts/dPCA.ipynb) - Dimensionality reduction using [dPCA](https://github.com/machenslab/dPCA).
  * [`TCA.ipynb`](scripts/TCA.ipynb) - Dimensionality reduction using [TCA](https://github.com/neurostatslab/tensortools) (more commonly known as the CP decomposition).
  * [`tensor_creation.ipynb`](scripts/tensor_creation.ipynb) - Code used after source extraction and before dimensionality reduction to perform additional component evaluation, time series alignment, and tensor creation.
* [`src`](src) - An auxiliary Python package used in the analysis pipeline.
  Custom hyperparameter classes and helper functions can be found here.
* [`tests`](tests) - Contains tests for some functions in the [`src`](src) package. 
  Currently, only one set of tests is included.
* [`environment.yml`](environment.yml) - Specifies all packages required by a conda environment to run the entire pipeline.
* [`environment_lin_lab_gpu.yml`](environment_lin_lab_gpu.yml) - Same as above but does not specify TensorFlow.
  This may fix problems during environment creation on the GPU in the Lin Lab.
* [`setup.py`](setup.py) - A setup script for the [`src`](src) package.



















