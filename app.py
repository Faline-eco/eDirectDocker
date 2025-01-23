from flask import Flask, request, jsonify
import subprocess
import shlex

app = Flask(__name__)

def common_to_scientific(common_name):
    """
    Function to run the NCBI EDirect command and parse the scientific name.
    """
    command = f'esearch -db taxonomy -query "{common_name}" | esummary | xtract -pattern DocumentSummary -element CommonName,ScientificName'
    try:
        # Use shell=True to allow pipe operators to work
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        if result.returncode != 0:
            return {"error": f"Command failed with error: {result.stderr.strip()}"}

        output_lines = result.stdout.strip().split("\n")
        results = []
        for line in output_lines:
            parts = line.split("\t")
            if len(parts) == 2:
                #results.append({"common_name": parts[0], "scientific_name": parts[1]})
                results.append(parts[1])

        return results if results else []

    except Exception as e:
        return {"error": str(e)}


@app.route("/com2sci", methods=["POST"])
def translate_names():
    """
    API endpoint to translate a list of common names to scientific names.
    """
    data = request.get_json()
    if not data or "common_names" not in data:
        return jsonify({"error": "Please provide a JSON object with a 'common_names' list."}), 400

    common_names = data["common_names"]
    if not isinstance(common_names, list):
        return jsonify({"error": "'common_names' should be a list."}), 400

    translations = {}
    for name in common_names:
        translations[name] = common_to_scientific(name)

    return jsonify(translations)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
