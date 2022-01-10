
_magnitudes = {"k": 1, "m": 2, "g": 3, "t": 4}
def size_str_to_int(size: str) -> int:
    size = size.lower()
    if size[-1] == "b":
        if size[-2] == "i":
            base = 1024
            mag = size[-3]
            rem = size[:-3]
        else:
            base = 1000
            mag = size[-2]
            rem = size[:-2]
        return int(float(rem) * (base ** _magnitudes.get(mag, 0)))
    else:
        return int(size)

_invert_mags = {0:"", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
def int_to_size_str(isize: int, ndigits: int = 2) -> str:
    mag = 0
    mag_max = max(_invert_mags.keys())
    while isize >= 1024 and mag < mag_max:
        isize = isize / 1024
        mag += 1
    return f"{round(isize, ndigits)} {_invert_mags[mag]}B"

