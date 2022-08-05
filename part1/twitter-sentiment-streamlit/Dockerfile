FROM python:3.10-slim-buster
COPY . /app
RUN mkdir -p /root/.streamlit
COPY ./config.toml /root/.streamlit/
COPY ./credentials.toml /root/.streamlit/
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 9001
ENTRYPOINT ["streamlit","run"]
CMD ["App_Streamlit.py"]
# streamlit-specific commands for config
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
