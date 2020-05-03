#Encoding Part
cd ./sender/encode/           &&  \
python3 run.py                &&  \
cd ../../sender/generateKey/  &&  \
python3 run.py                &&  \
#python3 run.py histogram      &&  \
#python3 run.py image          &&  \
#Encoding Completed

#Decoding Part
cd ../../receiver/getKey/     &&  \
python3 run.py                &&  \
cd ../../receiver/decode/     &&  \
python3 run.py
#Decoding Completed
