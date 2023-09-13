import subprocess
from os.path import exists

def test_runner():
    args = [
        "time",
        "python",
        "analysis/bfrag/run_xb.py",
        "analysis/bfrag/ttbar.json",
        "-x",
        "futures",
        "--hist-list",
        "xb_mass_d0"
        "--skip-cr",
        "-t",
        "-c",
        "1",
        "-o",
        "output_check_yields"
    ]

    # Run bfrag
    subprocess.run(args)

    assert (exists('histos/output_check_yields.pkl.gz'))
