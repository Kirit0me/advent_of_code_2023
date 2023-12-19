
from math import prod


def f1(k, xmas):
    if k in ("R", "A"):
        return k == "A"
    for p in d[k].split(","):
        match p.split(":"):
            case cond, dest:
                if eval(f"{xmas[cond[0]]}{cond[1:]}"):
                    return f1(dest, xmas)
            case dest,:
                return f1(dest, xmas)


def f2(k, lims):
    if k in ("R", "A"):
        if k == "R":
            return 0
        return prod(max(0, lims[f"{k}<"] - lims[f"{k}>"] - 1) for k in "xmas")
    o = 0
    for p in d[k].split(","):
        match p.split(":"):
            case cond, dest:
                ck = cond[:2]
                cv = (min, max)[cond[1] == ">"](int(cond[2:]), lims[ck])
                o += f2(dest, lims | {ck: cv})
                ck, cv = f"{ck[0]}{'<>'[ck[1]=='<']}", cv + (-1, 1)[ck[1] == ">"]
                lims[ck] = cv
            case dest,:
                o += f2(dest, lims)
    return o


a, b = open('aoc_in19.txt', 'r').read().split("\n\n")
d = {k: v[:-1] for k, v in (l.split("{") for l in a.splitlines())}
xs = (eval(l.replace("{", "dict(").replace("}", ")")) for l in b.splitlines())
print(sum(sum(x.values()) for x in xs if f1("in", x)))
print(f2("in", {f"{c}{o}": (0, 4001)[o == "<"] for c in "xmas" for o in "<>"}))
