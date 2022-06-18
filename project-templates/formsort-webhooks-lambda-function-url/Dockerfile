FROM public.ecr.aws/lambda/python:3.9
RUN pip install -U pip pipenv
WORKDIR ${LAMBDA_TASK_ROOT}
ARG PIPENV_FLAGS=""
COPY Pipfile Pipfile.lock ./
RUN pipenv lock ${PIPENV_FLAGS} -r | \
      sed 's@^-e @@' > requirements.txt && \
      pip install -r requirements.txt --target ${LAMBDA_TASK_ROOT} && \
      rm requirements.txt
COPY src src
COPY tests tests
