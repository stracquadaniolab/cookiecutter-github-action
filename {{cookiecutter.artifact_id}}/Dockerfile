FROM  debian:buster-slim

LABEL org.opencontainers.image.title="{{ cookiecutter.artifact_name }}"
LABEL org.opencontainers.image.description="{{ cookiecutter.artifact_description }}"
LABEL org.opencontainers.image.url="https://github.com/{{ cookiecutter.artifact_git }}"
LABEL org.opencontainers.image.documentation="https://github.com/{{ cookiecutter.artifact_git }}"
LABEL org.opencontainers.image.source="https://github.com/{{ cookiecutter.artifact_git }}"
LABEL org.opencontainers.image.revision="v0.0.0"
LABEL org.opencontainers.image.vendor="{{ cookiecutter.artifact_org }}"
LABEL org.opencontainers.image.authors="{{ cookiecutter.artifact_author }}"

ADD ./entrypoint.sh /usr/bin/entrypoint.sh

RUN chmod +x /usr/bin/entrypoint.sh

ENTRYPOINT [ "/usr/bin/entrypoint.sh" ]