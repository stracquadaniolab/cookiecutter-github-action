FROM stracquadaniolab/slim-container:latest

LABEL org.stracquadaniolab.maintainer="{{cookiecutter.artifact_id}}"
LABEL org.stracquadaniolab.version="0.0.1"
LABEL org.stracquadaniolab.platform="github-action"

ADD ./entrypoint.sh /usr/bin/entrypoint.sh

RUN chmod +x /usr/bin/entrypoint.sh

ENTRYPOINT [ "/usr/bin/entrypoint.sh" ]