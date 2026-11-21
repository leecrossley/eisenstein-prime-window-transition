"""Freshly compile and replay the finite trace statement over the pinned trace checkout."""
import argparse
import os
from pathlib import Path
import re
import subprocess
import tempfile

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("compiled_trace", type=Path, help="build directory produced by the pinned theta-prime-trace verifier")
    args = parser.parse_args()
    repo = Path(__file__).resolve().parent
    imports = args.compiled_trace.resolve()
    if not (imports/"ThetaPrimeTrace.olean").is_file():
        parser.error("the compiled directory must contain ThetaPrimeTrace.olean")
    commit="819816b2e0a3bf405af45ae5c7af2491d8f5bee6"
    version = subprocess.check_output(["lean","--version"], text=True)
    if commit not in version:
        raise RuntimeError("use pinned Lean 4.33.1")
    with tempfile.TemporaryDirectory() as fresh:
        previous=[str(Path(p).resolve()) for p in os.environ.get("LEAN_PATH","").split(os.pathsep) if p]
        env=dict(os.environ, LEAN_PATH=os.pathsep.join([fresh,str(imports),*previous]))
        compiler=subprocess.run(["lean","-R",str(repo),"-o",str(Path(fresh)/"EisensteinTrace.olean"),
                                 str(repo/"EisensteinTrace.lean")],env=env,cwd=repo,text=True,
                                stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        output=compiler.stdout
        if compiler.returncode:
            raise RuntimeError(output)
        names = ("EisensteinPrimeRace.trace_eq_norm_race", "EisensteinPrimeRace.no_quadratic_host")
        for name in names:
            check = re.search(re.escape(name) + r"' depends on axioms:\s*\[([^\]]*)\]", output)
            if not check or set(check[1].replace(" ", "").split(",")) != {"propext", "Classical.choice", "Quot.sound"}:
                raise RuntimeError(output)
        subprocess.run(["leanchecker","EisensteinTrace"],env=env,check=True)
    for name in names:
        print(f"Lean 4.33.1 kernel replay passed for {name}.")
    print("Reported axioms: propext, Classical.choice, Quot.sound.")

if __name__=="__main__":
    main()
