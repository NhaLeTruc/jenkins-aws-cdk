FROM jenkins/jenkins:lts

# Install custom plugins
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN jenkins-plugin-cli --plugin-file /usr/share/jenkins/ref/plugins.txt

COPY modify_casc.py /modify_casc.py
COPY config-as-code.j2 /config-as-code.j2

USER root

RUN apt-get update &&\
    apt-get install -y python3-pip &&\
    pip3 install --break-system-packages jinja2 dnspython &&\
    rm -rf /var/lib/apt/lists/* &&\
    touch /config-as-code.yaml &&\
    chown jenkins: /config-as-code.yaml &&\
    sed -i 's/\r//' /modify_casc.py &&\
    sed -i '/\/bin\/bash*/a \\n\/modify_casc.py' /usr/local/bin/jenkins.sh

# User back to jenkins
USER jenkins
