FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

ARG USERNAME=vscode
ARG USER_UID=1234
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
&& useradd --uid $USER_UID --gid $USER_GID -m -s /bin/bash $USERNAME

RUN pip install -r requirements.txt

CMD ["sleep", "infinity"]