#!/usr/bin/env python3
"""Check this kit's inline relative Markdown links and required document sections.
Usage: python3 check-links.py [kit-root] | --self-test
No network, installs, runtime imports, or file writes except temporary self-test files.
"""
from pathlib import Path
import re
import sys
import tempfile
from urllib.parse import unquote, urlsplit

LINK = re.compile(r'\[[^\]\n]+\]\(([^)\n]+)\)')
CAP_SECTIONS = (
    '목적과 사용 시점', '입력과 부족한 정보', '실행 단계', '산출물',
    '검증과 완료', '실패·보류·사람 확인', '다음 단계와 인계', '작은 작업에서 생략')


def check(root):
    root = root.resolve()
    files = sorted(root.rglob('*.md'))
    errors, count = [], 0
    if not files:
        return ['Markdown 파일 없음'], 0, 0
    for file in files:
        text = file.read_text(encoding='utf-8')
        for raw in LINK.findall(text):
            ref = urlsplit(raw.strip().strip('<>'))
            if ref.scheme or ref.netloc:
                continue
            target = (file.parent / unquote(ref.path)).resolve() if ref.path else file
            count += 1
            if not target.is_relative_to(root) or not target.is_file():
                errors.append(f'{file.relative_to(root)}: 잘못된 내부 경로 {raw}')
                continue
            # ponytail: package has simple inline links; use a Markdown parser if syntax expands.
            if ref.fragment:
                headings = re.findall(r'^#{1,6}\s+(.+)$', target.read_text(), re.M)
                slugs = {re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-') for h in headings}
                if unquote(ref.fragment) not in slugs:
                    errors.append(f'{file.relative_to(root)}: 없는 anchor {raw}')
        if file.parent == root / 'roles':
            for n in range(1, 11):
                if not re.search(rf'^## {n}\. ', text, re.M):
                    errors.append(f'{file.name}: 역할 항목 {n} 누락')
        if file.parent == root / 'capabilities':
            for heading in CAP_SECTIONS:
                if f'## {heading}\n' not in text:
                    errors.append(f'{file.name}: 기능 항목 {heading} 누락')
    return errors, len(files), count


def self_test():
    with tempfile.TemporaryDirectory(prefix='agent-kit-links-') as folder:
        root = Path(folder)
        (root / 'a.md').write_text('[good](b.md)\n')
        (root / 'b.md').write_text('# Target\n')
        assert not check(root)[0]
        (root / 'a.md').write_text('[missing](missing.md)\n[escape](../outside.md)\n[anchor](b.md#nope)\n')
        assert len(check(root)[0]) == 3
    print('self-test: valid link accepted; missing/escape/anchor rejected')


if __name__ == '__main__':
    if sys.argv[1:] == ['--self-test']:
        self_test()
    else:
        base = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
        failures, files, links = check(base)
        for failure in failures:
            print(failure)
        print(f'{files} Markdown files; {links} relative links; {len(failures)} errors')
        sys.exit(bool(failures))
