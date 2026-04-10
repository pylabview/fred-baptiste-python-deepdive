# 11_creating_ditcs.py
import logging

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S",
)


logger.info("Creating dicts using literals\n")
a = {"k1": 100, "k2": 200}
# breakpoint()
print(type(a["k1"]))
logger.info("We can use hashable objects as keys in dictionaries\n")
t1 = (1, 2, 3)  # this is a tuple
# breakpoint()
print(f"t1 is a {type(t1)}, and is hashable {hash(t1)}")

d = {t1: "this is a tuple"}
print(f"{logger.info('this is d uisng t1 as a key')} -> {d}")
print(f"Accessing the dict d members using t1 {d[t1]}")
