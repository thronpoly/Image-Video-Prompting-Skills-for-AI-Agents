#!/usr/bin/env python3
"""Install the bundled prompt skills locally. Standard library only; no downloads."""
import argparse
from datetime import datetime
import hashlib
import json
from pathlib import Path
import shutil
import sys

PACKAGE=Path(__file__).resolve().parent
def verify():
    manifest=json.loads((PACKAGE/'MANIFEST.json').read_text(encoding='utf-8'))
    for item in manifest['files']:
        path=PACKAGE/item['path']
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest()!=item['sha256']:
            raise ValueError('Package file is missing or changed: '+item['path'])
    return manifest

def linked(path):
    return path.is_symlink() or getattr(path,'is_junction',lambda:False)()

def ensure_plain_tree(path, boundary):
    resolved=path.resolve()
    try:resolved.relative_to(boundary.resolve())
    except ValueError:raise ValueError('Destination escapes selected root: '+str(path))
    current=path
    while current != boundary:
        if linked(current):raise ValueError('Refusing a symlink/junction destination: '+str(current))
        if current.parent==current:raise ValueError('Cannot establish destination boundary')
        current=current.parent
    if linked(boundary):raise ValueError('Selected root must not be a symlink/junction')
    if path.exists():
        for child in path.rglob('*'):
            if linked(child):raise ValueError('Refusing a linked existing file: '+str(child))

def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--client',choices=['codex','claude','both'])
    parser.add_argument('--scope',choices=['project','user'],default='project')
    parser.add_argument('--project',type=Path,help='Existing target project; required for project scope')
    parser.add_argument('--skills',nargs='+',help='Optional subset of bundled skill names')
    parser.add_argument('--dry-run',action='store_true',help='Show changes without writing')
    parser.add_argument('--replace',action='store_true',help='Back up same-name skills, then overlay package files')
    parser.add_argument('--verify',action='store_true',help='Verify package hashes and exit')
    args=parser.parse_args(argv)
    try:
        manifest=verify()
        if args.verify:
            print('Verified {} package files.'.format(len(manifest['files'])))
            return 0
        if not args.client:parser.error('--client is required unless --verify is used')
        if args.scope=='project':
            if args.project is None:parser.error('--project is required for project scope')
            boundary=args.project.expanduser().absolute()
            if not boundary.is_dir():raise ValueError('Target project directory does not exist: '+str(boundary))
        else:
            if args.project is not None:parser.error('--project applies only to project scope')
            boundary=Path.home().absolute()
        available=manifest['skills']
        selected=args.skills or available
        unknown=set(selected)-set(available)
        if unknown:raise ValueError('Unknown skills: '+', '.join(sorted(unknown)))
        selected=list(dict.fromkeys(selected))
        clients=['codex','claude'] if args.client=='both' else [args.client]
        jobs=[]
        stamp=datetime.now().strftime('%Y%m%d-%H%M%S-%f')
        for client in clients:
            root=boundary/('.agents' if client=='codex' else '.claude')/'skills'
            for name in selected:
                source=PACKAGE/'skills'/name;target=root/name
                ensure_plain_tree(target,boundary)
                if target.exists() and not target.is_dir():raise ValueError('A non-directory occupies: '+str(target))
                if target.exists() and not args.replace:raise ValueError('Skill already exists; use --replace after review: '+str(target))
                backup=boundary/'.prompt-skills-backups'/stamp/client/name
                ensure_plain_tree(backup,boundary)
                jobs.append((source,target,backup))
        for source,target,backup in jobs:
            print(('PLAN ' if args.dry_run else 'INSTALL ')+str(target))
            if target.exists():print('BACKUP '+str(backup))
        if args.dry_run:
            print('Dry run complete. No files written.')
            return 0
        for source,target,backup in jobs:
            if target.exists():
                backup.parent.mkdir(parents=True,exist_ok=True)
                shutil.copytree(target,backup)
            target.parent.mkdir(parents=True,exist_ok=True)
            shutil.copytree(source,target,dirs_exist_ok=True)
        print('Installed {} skill folder(s). Reload/restart the client if needed.'.format(len(jobs)))
        return 0
    except (OSError,ValueError,KeyError) as error:
        print('ERROR: '+str(error),file=sys.stderr)
        return 1

if __name__=='__main__':sys.exit(main())
