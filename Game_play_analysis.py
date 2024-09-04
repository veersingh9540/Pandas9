import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
  DF = activity.groupby('player_id')['event_date'].min().reset_index()
  
  return DF.rename(columns= {'event_date': "first_login"})