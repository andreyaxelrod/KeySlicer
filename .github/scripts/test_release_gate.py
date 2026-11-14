import base64, datetime, importlib.util, json, pathlib, subprocess, tempfile, unittest
from unittest.mock import patch
from cryptography.exceptions import InvalidSignature
ROOT=pathlib.Path(__file__).resolve().parents[1]
GATE=ROOT/'Scripts/ci/public-gate.py'
# Same tests can be installed in the public controller without private sources.
if not GATE.exists(): GATE=pathlib.Path(__file__).with_name('release-gate.py')
spec=importlib.util.spec_from_file_location('gate',GATE);gate=importlib.util.module_from_spec(spec);spec.loader.exec_module(gate)

class ReleaseGateTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup);self.root=pathlib.Path(self.temp.name)
        from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
        self.key=Ed25519PrivateKey.generate()
        public=self.key.public_key().public_bytes_raw()
        self.patch=patch.object(gate,'PUBLIC_KEY',base64.b64encode(public).decode());self.patch.start();self.addCleanup(self.patch.stop)
        self.good={'schema':1,'repository':'andreyaxelrod/KeySlicer','version':'1.0.99','build':'100','draft_id':123,
                   'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
                   'checks':{k:True for k in gate.REQUIRED},
                   'assets':{n:{'size':10,'sha256':'a'*64} for n in ['KeySlicer-1.0.99.dmg','appcast.xml','FFmpeg-source.zip']}}
    def signed(self,e):
        data=json.dumps(e).encode()
        signature=self.key.sign(data)
        return base64.b64encode(data).decode(),base64.b64encode(signature).decode()
    def test_valid_approval(self):self.assertEqual(gate.validate(*self.signed(self.good)),self.good)
    def test_rejects_unsigned_or_modified_payload(self):
        payload,sig=self.signed(self.good)
        for p,s in [(payload,base64.b64encode(b'x'*64).decode()),(base64.b64encode(b'{}').decode(),sig)]:
            with self.assertRaises((ValueError,AssertionError,InvalidSignature)):gate.validate(p,s)
    def test_rejects_missing_failed_expired_wrong_repository_and_extra_assets(self):
        mutations=[{'checks':{}},{'checks':dict(self.good['checks'],native=False)},
                   {'created_utc':'2000-01-01T00:00:00+00:00'},{'repository':'attacker/repo'},
                   {'assets':dict(self.good['assets'],**{'source.zip':{'size':10,'sha256':'a'*64}})}]
        for change in mutations:
            with self.subTest(change=change),self.assertRaises((AssertionError,ValueError)):
                gate.validate(*self.signed(dict(self.good,**change)))
    def test_final_launch_and_update_cannot_be_omitted(self):
        for key in ['final_launch','update_install','signing']:
            e=dict(self.good);e['checks']=dict(self.good['checks']);del e['checks'][key]
            with self.assertRaises(AssertionError):gate.validate(*self.signed(e))

if __name__=='__main__':unittest.main()
