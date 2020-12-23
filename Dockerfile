FROM SKYLORD-OP-op/SKYLORD-OP_op:latest

#clonning repo 
RUN git clone https://github.com/SKYLORD-OP-op/SKYLORD-OP_op.git/root/userbot
#working directory 
WORKDIR /root/userbot

# Install requirements
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/userbot/bin:$PATH"

CMD ["bash","startup.sh"]
