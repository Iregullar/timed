import os 
from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("session_name", "BAGANPEAfKgQtKlGeT_B-Pv3nZf_jY2Wiit_KyGMcm_G_32SBjaOkUNC8Kd5u-bgcJ_3fZ37Ny7MrkhJK2SqRcq-eMKMtJGl_NUVyCxiKuUVSsROqP2zwfg5YK930jbFHVe_Kmw73AmIMAdYHcS014_yVqqq0B-oJ9xJRqgYqzvrfCWcPK8fov88uK9c3iiGDHZ490G9zyCxGQJ9Vv7JdrClq8LGlawzl3BbPcQ5kAPpm2FsFSbS3DL8DPkNLdTgIWazdSIFwrOxnxdkbZNng9vNKJtkrpr7vB_N4Xymx5EyznUHU6I0sp5Mxgs-Oaq5a8cyLAYEIpA7-Kc-er81L19eLFmtfQAAAAGbo6nbAA")
API_ID = int(getenv("api_id", "25179377"))
API_HASH = getenv("api_hash", "8c0bd3df9ebe3750cfe0dfe34bcf53a4")
CHANNEL_ID = getenv("channel_id", "-1002287843270")
last_messages_amount = 50 
