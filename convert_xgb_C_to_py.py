# convert_xgb_C_to_py.py
import json

def build_tree(tree):
    """
    Convert one tree from XGBoost's old internal JSON format
    into Python decision code.
    """

    num_nodes = int(tree["tree_param"]["num_nodes"])
    left = tree["left_children"]
    right = tree["right_children"]
    split_index = tree["split_indices"]
    split_cond = tree["split_conditions"]
    base_weights = tree["base_weights"]  # leaf values stored here!

    def dfs(node, indent=0):
        space = " " * indent

        # leaf node if no children
        if left[node] == -1 and right[node] == -1:
            leaf_value = base_weights[node]
            return f"{space}return {leaf_value}\n"

        # internal node
        feature = split_index[node]
        threshold = split_cond[node]

        code = (
            f"{space}if features[{feature}] < {threshold}:\n" +
            dfs(left[node], indent + 4) +
            f"{space}else:\n" +
            dfs(right[node], indent + 4)
        )
        return code

    return dfs(0)


def convert():
    model = json.load(open("xgb_C.json"))
    trees = model["learner"]["gradient_booster"]["model"]["trees"]

    out = "def xgb_predict(features):\n    score = 0.0\n\n"

    for i, tree in enumerate(trees):
        out += f"    # Tree {i}\n"
        out += f"    def t{i}(features):\n"
        body = build_tree(tree)
        out += body.replace("\n", "\n        ")
        out += "\n"
        out += f"    score += t{i}(features)\n\n"

    out += "    return score\n"

    with open("xgb_predict_C.py", "w") as f:
        f.write(out)

    print("Saved xgb_predict_C.py")


if __name__ == "__main__":
    convert()
