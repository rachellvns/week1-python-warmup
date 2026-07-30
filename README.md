Overview:
This repository contains Python warmup exercises, covering data validation using Pydantic models and asynchronous programming using Python's asyncio library.
The goal of these katas (async_kata & pydantic_kata) is validating structured data/JSON, handling asynchronous tasks, and controlling concurrency.

Repository Contents:

    1) pydantic_kata.py -> demonstrates building data models using Pydantic
    Implementation: create models using BaseModel, apply field constraint, demo good & bad payload, use model_validator for model-level validation, validate JSON input, use nested model.
    Use case: Creating SEO audit models with 3 pillars (technical, on-page, off-page)
    2) async_kata.py -> demonstrates asynchronous programming using asyncio.
    Implementation: create async functions with async def, using await for async operations, running multiple tasks concurrently with asyncio.gather(), measuring execution time with time.perf_counter(), limiting concurrent tasks using asyncio.Semaphore
    Use case: simulating concurrent data fetching from multiple sources while controlling the number of active tasks.

Setup steps:
1. Clone the repo:
git clone https://github.com/rachellvns/week1-python-warmup.git 
cd week1-python-warmup
2. Create and activate a virtual environment:
uv venv
source .venv/Scripts/activate
3. Install dependencies:
uv pip install pydantic python-dotenv
4. Create a '.env' file in the project root
5. Run the katas:
python pydantic_kata.py
python async_kata.py

Setup Experience
Most of my setup friction came from Git and shell inconsistencies rather than the Python side. Early on, I mixed up '.env' (secrets) with '.venv' (virtual environment) and later hit a confusing moment where my '.gitignore' showed as 'deleted' after switching branches, which turned out to be because I had originally created it while standing in the parent folder instead of the project folder.
The most useful habit I picked up was checking 'git status' before every commit, to make sure I don't commit confidential file/folder.