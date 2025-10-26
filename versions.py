import importlib.metadata
packages = [
    "python-dotenv",
    "fastapi",
    "ipykernel",
    "langgraph",
    "langchain",
    "langchain-astradb",
    "langchain-core",          # or "langchain_core" if metadata complains
    "langchain-google-genai",
    "langchain-groq",
    "langchain-openai",
    "langchain-mcp-adapters",
    "mcp",
    "langchain_community",
    "structlog",
    "langchain_core",
    "tavily-python",           # if error, try "tavily_python"
    "wikipedia",
    "pydantic",
    "python-docx",
    "reportlab",
    "fastapi",
    "uvicorn",
    "jinja2",
    "httpx",
    "aiofiles",
    "sqlalchemy" 
]
for pkg in packages:
    try:
        version = importlib.metadata.version(pkg)
        print(f"{pkg}=={version}")
    except importlib.metadata.PackageNotFoundError:
        
        print(f"{pkg} (not installed)")

# # serve static & templates
# app.mount("/static", StaticFiles(directory="../static"), name="static")
# templates = Jinja2Templates(directory="../templates")