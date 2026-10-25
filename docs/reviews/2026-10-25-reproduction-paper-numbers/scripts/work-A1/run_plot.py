"""Run the committed plot_removal.py unchanged except for its two paths: read the
committed removal_ci.json, write into work-A1/figures/."""
import sys, types, importlib.util
from pathlib import Path
clone, outdir = Path(sys.argv[1]), Path(sys.argv[2])
sys.path.insert(0, str(clone / "src"))
spec = importlib.util.spec_from_file_location("plot_removal", clone / "experiments/01-self-indexing-removal-test/src/plot_removal.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
m.CI_FILE = clone / "experiments/01-self-indexing-removal-test/removal_ci.json"
m.FIG_DIR = outdir
m.main()
