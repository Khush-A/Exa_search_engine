import os

from flask import Flask, render_template, request
from exa_py import Exa

app = Flask(__name__)

EXA_API_KEY = os.environ.get("EXA_API_KEY")
if not EXA_API_KEY:
    raise RuntimeError("EXA_API_KEY environment variable not set")

exa = Exa(EXA_API_KEY)


@app.route("/", methods=["GET", "POST"])
def index():
    query = ""
    domain = ""
    results = []
    error = None
    num_results = 10

    if request.method == "POST":
        query = request.form.get("query", "").strip()
        domain = request.form.get("domain", "").strip()
        num_results = int(request.form.get("num_results", 10))

        if not query:
            error = "Please enter a search query."
        else:
            try:
                mode = request.form.get("mode", "web")

                search_kwargs = dict(
                    num_results=num_results,
                    type="keyword",
                )
                if mode == "tiktok":
                    search_kwargs["include_domains"] = ["www.tiktok.com"]
                elif mode == "youtube":
                    search_kwargs["include_domains"] = ["www.youtube.com", "youtu.be"]
                else:
                    if domain:
                        search_kwargs["include_domains"] = [domain]

                response = exa.search(query, **search_kwargs)
                results = response.results

            except Exception as e:
                # basic error handling for now
                error = f"Something went wrong: {e}"

    return render_template(
        "index.html",
        query=query,
        domain=domain,
        results=results,
        error=error,
        num_results=num_results
    )


if __name__ == "__main__":
    app.run(debug=True)
