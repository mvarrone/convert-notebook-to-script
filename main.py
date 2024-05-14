import os
import json


def convert_ipynb_to_py(notebook_path, output_path):
    # Read the notebook
    with open(notebook_path, "r", encoding="utf-8") as f:
        nb = json.load(f)

    # Create the output directory if it does not exist
    os.makedirs(output_path, exist_ok=True)

    # Extract the notebook name without the extension
    notebook_name = os.path.splitext(os.path.basename(notebook_path))[0]
    py_file_path = os.path.join(output_path, notebook_name + ".py")

    # Open the .py file to write
    with open(py_file_path, "w", encoding="utf-8") as py_file:
        for cell in nb.get("cells", []):
            if cell.get("cell_type") == "markdown":
                continue
                # Write markdown cells as comments
                for line in cell.get("source", []):
                    py_file.write("# " + line + "\n")
                py_file.write("\n")
            elif cell.get("cell_type") == "code":
                # Write code cells as is
                for line in cell.get("source", []):
                    py_file.write(line + "\n")
                py_file.write("\n")


def main() -> None:
    input_folder = "inputs"
    output_folder = "outputs"

    # Ensure the input folder exists
    if not os.path.exists(input_folder):
        print(f"The input folder '{input_folder}' does not exist.")
        return

    if not os.listdir(input_folder):
        print(f"No .ipynb files inside folder called {input_folder}")
        return

    # Process each .ipynb file in the input folder
    for notebook_file in os.listdir(input_folder):
        if notebook_file.endswith(".ipynb"):
            notebook_path = os.path.join(input_folder, notebook_file)
            convert_ipynb_to_py(notebook_path, output_folder)
            print(f"Converted '{notebook_file}' to Python script.")


if __name__ == "__main__":
    main()
