FROM python:3.11

# install python package
COPY pyproject.toml ./
RUN pip install poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --with test,lint,simple

# mount dir
RUN mkdir -p /opt/mnt
WORKDIR /opt/mnt

# copy all files into container
COPY . /opt/mnt

# expose port
EXPOSE 8888