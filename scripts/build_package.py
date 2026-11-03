"""Rebuild Claude archives, hashes and the standalone package. No downloads."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
TOP_FILES = ['README.md', 'USAGE_KO.md', 'PROJECT_INSTRUCTIONS.md', 'install.py']


def zip_bytes(files):
    from io import BytesIO
    buffer = BytesIO()
    with zipfile.ZipFile(buffer, 'w', zipfile.ZIP_DEFLATED) as archive:
        for name, content in sorted(files.items()):
            info = zipfile.ZipInfo(name, (2026, 11, 3, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, content)
    return buffer.getvalue()


def collect(directory):
    return {p.relative_to(ROOT).as_posix(): p.read_bytes()
            for p in (ROOT / directory).rglob('*')
            if p.is_file() and '__pycache__' not in p.parts
            and p.suffix != '.pyc'}


def manifest(files, skills, version):
    return (json.dumps({
        'name': 'team-prompt-skills', 'version': version,
        'manuals_checked': '2026-11-03', 'skills': skills,
        'files': [{'path': name, 'size': len(data),
                   'sha256': hashlib.sha256(data).hexdigest()}
                  for name, data in sorted(files.items())]
    }, ensure_ascii=False, indent=2) + '\n').encode('utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--version', default='1.1.0')
    args = parser.parse_args()
    if not re.fullmatch(r'\d+\.\d+\.\d+', args.version):
        parser.error('Use a numeric semantic version, such as 1.1.0')
    skills = sorted(p.name for p in (ROOT / 'skills').iterdir()
                    if (p / 'SKILL.md').is_file())
    uploads = ROOT / 'claude-upload'
    uploads.mkdir(exist_ok=True)
    for name in skills:
        files = {path[len('skills/'):]: data
                 for path, data in collect('skills/' + name).items()}
        (uploads / (name + '.zip')).write_bytes(zip_bytes(files))
    files = {name: (ROOT / name).read_bytes() for name in TOP_FILES}
    for directory in ['skills', 'claude-upload', 'scripts', 'evals']:
        files.update(collect(directory))
    (ROOT / 'MANIFEST.json').write_bytes(manifest(files, skills, args.version))
    # Standalone archives have their own README link and matching manifest.
    archive_name = 'team-prompt-skills-v' + args.version
    download_path = 'downloads/' + archive_name + '.zip'
    readme = files['README.md'].decode('utf-8').replace(
        '](' + download_path + ')',
        '](https://github.com/thronpoly/Image-Video-Prompting-Skills-for-AI-Agents/blob/main/' + download_path + ')')
    files['README.md'] = readme.encode('utf-8')
    files['MANIFEST.json'] = manifest(files, skills, args.version)
    target = ROOT / download_path
    target.parent.mkdir(exist_ok=True)
    target.write_bytes(zip_bytes({archive_name + '/' + k: v for k, v in files.items()}))
    print('Built {} skills; {} files; {}'.format(len(skills), len(files), target.name))


if __name__ == '__main__':
    main()
