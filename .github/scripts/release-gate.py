#!/usr/bin/env python3
"""Public-only release controller. Contains no private source or signing secrets."""
import base64, datetime, hashlib, json, os, pathlib, re, subprocess, tempfile
PUBLIC_KEY = 'a41L8rrGO5Dk88dazbS5T9TQpu9KrgkLMJU0xdc1nh8='
REPO = 'andreyaxelrod/KeySlicer'
REQUIRED = {'inputs', 'native', 'preflight', 'signing', 'final_launch', 'update_install', 'artifact_verification'}

def run(*args):
    return subprocess.check_output(args, text=True).strip()

def validate(payload, signature, now=None):
    raw = base64.b64decode(payload, validate=True)
    sig = base64.b64decode(signature, validate=True)
    if len(raw) > 16000 or len(sig) != 64: raise ValueError('Invalid approval size')
    from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
    Ed25519PublicKey.from_public_bytes(base64.b64decode(PUBLIC_KEY)).verify(sig, raw)
    e = json.loads(raw)
    assert e['schema'] == 1 and e['repository'] == REPO
    assert re.fullmatch(r'\d+\.\d+\.\d+', e['version']) and str(e['build']).isdigit()
    assert type(e['draft_id']) is int and e['draft_id'] > 0
    now = now or datetime.datetime.now(datetime.timezone.utc)
    stamp = datetime.datetime.fromisoformat(e['created_utc'])
    assert 0 <= (now-stamp).total_seconds() <= 3600, 'Expired/future release approval'
    assert set(e['checks']) == REQUIRED and all(v is True for v in e['checks'].values())
    expected = {f"KeySlicer-{e['version']}.dmg", 'appcast.xml', 'FFmpeg-source.zip'}
    assert set(e['assets']) == expected
    for v in e['assets'].values():
        assert re.fullmatch('[0-9a-f]{64}', v['sha256']) and type(v['size']) is int and v['size'] > 0
    return e

def main():
    e = validate(os.environ['APPROVAL_B64'], os.environ['APPROVAL_SIGNATURE'])
    draft = json.loads(run('gh','api',f"repos/{REPO}/releases/{e['draft_id']}"))
    assert draft['draft'] and not draft['prerelease'] and draft['tag_name'] == 'v'+e['version']
    assert {a['name'] for a in draft['assets']} == set(e['assets'])
    latest = json.loads(run('gh','api',f'repos/{REPO}/releases/latest'))
    assert tuple(map(int,e['version'].split('.'))) > tuple(map(int,latest['tag_name'].removeprefix('v').split('.')))
    with tempfile.TemporaryDirectory() as d:
        for a in draft['assets']:
            expected = e['assets'][a['name']]
            assert a['size']==expected['size'] and a['digest']=='sha256:'+expected['sha256']
            with open(pathlib.Path(d)/a['name'], 'wb') as f:
                subprocess.run(['gh','api',f"repos/{REPO}/releases/assets/{a['id']}",'-H','Accept: application/octet-stream'],stdout=f,check=True)
            data=(pathlib.Path(d)/a['name']).read_bytes()
            assert len(data)==expected['size'] and hashlib.sha256(data).hexdigest()==expected['sha256']
    if os.environ.get('PUBLISH') == 'true':
        # Tag creation is allowed only to this repository's Actions integration.
        run('gh','release','edit','v'+e['version'],'--draft=false','--latest','--repo',REPO)
        latest=json.loads(run('gh','api',f'repos/{REPO}/releases/latest'))
        assert latest['id']==e['draft_id'] and not latest['draft']
    print('Signed approval and exact release assets verified' + ('; published' if os.environ.get('PUBLISH')=='true' else ''))

if __name__=='__main__': main()
