import pickle
from himpy.histogram import operations, expressionOperations
from himpy.executor import Parser, Evaluator
from himpy.utils import E
from utils.search_engine import SearchEngine

parser = Parser()
Ec_green        = E("e1+e2+e3+e4+e5+e6+e7+e8+e9+e10+e11+e12+e13+e14+e15+e16+e17+e18+e19+e20")
Ec_yellow_green = E("e2+e3+e21+e22+e23+e24+e25+e26+e27+e28+e29+e30")
Ec_red          = E("e31+e32+e33+e34+e35+e36+e37+e38+e39+e40")
Ec_rose         = E("e32+e35+e36+e39+e40")
Ecs = [
    ("green", Ec_green),
    ("yellow_green", Ec_yellow_green),
    ("red", Ec_red),
    ("rose", Ec_rose)
]
high_level_elements = { name: parser.parse_set(Ec.value) for name, Ec in Ecs}

with open("hists.pkcl", "rb") as f:
    hists = pickle.load(f)
with open("images.pkcl", "rb") as f:
    images = pickle.load(f)

evaluator = Evaluator(operations, expressionOperations, high_level_elements=high_level_elements)
search_engine_default = SearchEngine(hists, parser, evaluator, use_index=False)
search_engine_inverted_index = SearchEngine(hists, parser, evaluator, use_index=True)

TOP_N = 20

E1 = E("green")
E2 = E("yellow_green")
E3 = E("red")
E4 = E("rose")
E5 = E("any")

query = E1 * E('e1+e2+e3')

ranked_images = search_engine_inverted_index.retrieve(query, top_n=1000)
print("Total retrieved images:", len(ranked_images))
ranked_images[:5]