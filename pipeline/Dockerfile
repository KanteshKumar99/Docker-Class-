from  python:3.10.0 
# we are get base image

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/ 
# get binarry of uv packages


WORKDIR /app #make app darictry

ENV PATH="/app/.venv/bin:$PATH" 
#set path

copy ".python-version" "pyproject.toml" "uv.lock" ./
#copy files

RUN uv sync --locked
#files locked and sync

copy pipeline.py pipeline.py
#our running file can copy it.

ENTRYPOINT ["uv", "run", "python", "pipeline.py" ]


# this whole code means which code darict, now it can run with packages 