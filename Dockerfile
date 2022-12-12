FROM python:3.7

EXPOSE 8501

RUN mkdir Breton-Password-Generator

WORKDIR Breton-Password-Generator

COPY . .

RUN python3 -m pip install -r requirement.txt

ENTRYPOINT [ "streamlit", "run" ]
CMD [ "web/web.py", "--server.headless", "true", "--server.fileWatcherType", "none", "--browser.gatherUsageStats", "false"]