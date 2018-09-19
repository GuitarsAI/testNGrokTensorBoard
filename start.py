get_ipython().system_raw('tensorboard --logdir="./dire" --host 0.0.0.0 --port 6006 &')
get_ipython().system_raw('./ngrok http 6006 &')
