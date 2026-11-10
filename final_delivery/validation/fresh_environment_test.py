from pathlib import Path
import importlib.util
import ast

PROJECT_ROOT = Path(
    r"C:\Users\hp\Nassau_Candy_Final_Submission"
)
APP_ROOT = PROJECT_ROOT / "data" / "processed" / "app_bundle"
APP_FILE = APP_ROOT / "app.py"

packages = [
    "pandas", "numpy", "sklearn", "joblib",
    "streamlit", "plotly", "openpyxl"
]

failed = []

print("=" * 60)
print("FRESH ENVIRONMENT VALIDATION")
print("=" * 60)

for package in packages:
    available = importlib.util.find_spec(package) is not None
    print(package, "PASS" if available else "FAIL")
    if not available:
        failed.append(package)

if APP_FILE.exists():
    try:
        ast.parse(APP_FILE.read_text(encoding="utf-8"))
        print("Application syntax: PASS")
    except Exception as error:
        print("Application syntax: FAIL", error)
        failed.append("application syntax")
else:
    print("Application file: FAIL")
    failed.append("app.py")

for module in [
    "prediction_utils.py",
    "feature_utils.py",
    "scenario_utils.py",
    "recommendation_utils.py"
]:
    candidates = [
        APP_ROOT / "src" / module,
        APP_ROOT / module
    ]
    found = any(path.exists() for path in candidates)
    print(module, "PASS" if found else "REVIEW REQUIRED")

print("STATUS:", "PASS" if not failed else "FAIL")
if failed:
    print("Failed checks:", failed)