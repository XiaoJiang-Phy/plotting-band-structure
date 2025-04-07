# Plotting Band Structure

This repository provides a set of Python scripts for plotting the band structure of materials. The band structure data is processed by `vaspkit` after performing a `VASP` calculation.

## Overview

This tool allows you to visualize the band structure by using the data processed from `vasp` calculations. The script works with band structure data in the format provided by `vaspkit` and can plot both spin-polarized and non-spin-polarized band structures.

## File Structure

- `.github/workflows`: Contains the GitHub actions for continuous integration.
- `Band_100.pdf`: A PDF representation of a specific band structure plot.
- `Band_100.png`: A PNG representation of the same band structure plot.
- `KLABELS`: Contains the k-point labels for the band structure.
- `LICENSE`: The license for this repository.
- `REFORMATTED_BAND.dat`: The reformatted band data to be used in plotting.
- `band-spin.py`: Python script to plot the spin-polarized band structure.
- `band.py`: Python script to plot the non-spin-polarized band structure.
- `README.md`: Documentation for the project.

## Installation

### Prerequisites

- Python 3.x
- `matplotlib` for plotting
- `numpy` for numerical operations
- `pandas` for data handling

### Steps to Install

1. Clone the repository:
    ```bash
    git clone https://github.com/XiaoJiang-Phy/plotting-band-structure.git
    ```

2. Navigate to the project directory:
    ```bash
    cd plotting-band-structure
    ```

3. Install the required Python libraries:
    ```bash
    pip install matplotlib numpy pandas
    ```

## Usage

### Step 1: Prepare the input files

Before running the scripts, ensure that you have the following files:
- `REFORMATTED_BAND.dat`: The reformatted band data from `vaspkit`.
- `KLABELS`: The k-point labels for the band structure.

### Step 2: Run the Python script

To plot a non-spin-polarized band structure, run the `band.py` script:

```bash
python3 band.py

For a spin-polarized band structure, run the `band-spin.py` script:
```bash
python3 band-spin.py

## Example

### Iuput files:

- `REFORMATTED_BAND.dat`: The reformatted data for plotting the band structure.
- `KLABELS`: The file with k-point labels used in the plot.

### Output:

- `Band_100.pdf`: A PDF plot of the band structure.
- `Band_100.png`: A PNG plot of the band structure.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

