import subprocess as sp
import shlex


sp.call(shlex.split("streamlit run model_management.py"), shell=True)