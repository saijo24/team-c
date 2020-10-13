import basicClass as bc
import manageData as md

def init_database(users: list):
  md.InitDatas(users)

def weight_calc(data: dict, user: str):
  bc.Assem(data, user)

def fine_database(users: list):
  md.FineDatas(users)