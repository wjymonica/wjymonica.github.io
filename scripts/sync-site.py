#!/usr/bin/env python3
"""Compare or copy shared site files to a second local repository checkout."""
import argparse
from pathlib import Path
import shutil
import subprocess

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('target', type=Path, help='Path to the other repository checkout')
parser.add_argument('--apply', action='store_true', help='Copy changed shared files (default: check only)')
args = parser.parse_args()
source = Path(__file__).resolve().parents[1]
target = args.target.resolve()
if source == target or not (target / '.git').exists():
    parser.error('Target must be a different Git checkout.')
allowed = ('wjymonica/wjymonica.github.io', 'wjymonica/jingyingwang.github.io')
remote = subprocess.check_output(['git', '-C', str(target), 'remote', 'get-url', 'origin'], text=True).strip()
if not any(remote.removesuffix('.git').endswith('/' + repo) or remote.removesuffix('.git').endswith(':' + repo) for repo in allowed):
    parser.error('Target origin must be one of the two personal website repositories.')
files = [Path(name) for name in ('index.html', 'styles.css', '.nojekyll', 'README.md', 'scripts/sync-site.py')]
files += [p.relative_to(source) for p in (source / 'img').rglob('*') if p.is_file()]
changed = []
for relative in files:
    src, dst = source / relative, target / relative
    if src.is_symlink() or dst.is_symlink() or not dst.resolve().is_relative_to(target):
        parser.error(f'Refusing symlink or escaping destination: {relative}')
    if not dst.is_file() or src.read_bytes() != dst.read_bytes():
        changed.append(relative)
        print(('Copy: ' if args.apply else 'Different: ') + str(relative))
        if args.apply:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
print(f'{len(changed)} shared file(s) ' + ('copied.' if args.apply else 'differ.'))
if changed and not args.apply:
    raise SystemExit(1)
