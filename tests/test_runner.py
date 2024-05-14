'''
Tests for repo
'''
import subprocess
from os.path import exists

def test_runner():
    '''
    Test run_xb.py
    '''
    args = [
        "time",
        "python",
        "analysis/bfrag/run_xb.py",
        "analysis/bfrag/ttbar.json",
        "-x",
        "futures",
        "--hist-list",
        "xb_mass_d0",
        "--skip-cr",
        "-t",
        "-c",
        "1",
        "-p",
        "analysis/bfrag/histos/",
        "-o",
        "output_check_yields"
    ]

    # Run bfrag
    subprocess.run(args, check=False)

    assert exists('analysis/bfrag/histos/output_check_yields.pkl')
