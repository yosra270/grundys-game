clean:
    rm -rf __pycache__

setup: requirements.txt
    pip install -r requirements.txt

run: clean
    python src/runner.py