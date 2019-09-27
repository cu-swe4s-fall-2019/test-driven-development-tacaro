# test-driven-dev
Test Driven Development

Here we use randomly generated data to create histograms, box plots, and a combination of the two, displaying mean and standard deviation statistics.

## Files
### viz.py
This is our main script that is executed. viz.py takes in data through stdin and generates a plot as defined by a user. The function takes two arguments:
--out_file: the desired name of your output file
--plot_type: the type of plot you would like. Accepts 'hist', 'box', or 'combo'
These are abbreviated as -o and -p, respectively.

To test the functionality of viz.py, we use...
### gen_data.sh
This creates a two-column array with random integers. These can be fed into viz.py using pipe notation:
`bash gen_data.sh | python viz.py -o hist.png -p hist`

This command will generate a histogram called hist.png in your current working directory.

### tests.py
Includes unittests for mean, standard deviation methods within math_lib.py
Includes unittests for data_viz.py, making sure that the module can handle bad data.

### get_data.py
A module that includes read_stdin_col, a method that intakes an array through stdin and returns a numpy array containing a pre-defined column.

# Installation
pycodestyle is required to run the verification tests:
`pip install pycodestyle
pip install --upgrade pycodestyle
pip uninstall pycodestyle`

Future functional testing may involve ssshtest, which can be installed with:
`test -e ssshtest || wget -qhttps://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest`

Matplotlib is required and can be installed with:
`conda activate swe4s
conda install matplotlib`
