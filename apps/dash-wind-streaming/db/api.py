import pandas as pd
import psycopg2




def getdata():
    ENDPOINT = "derp8-aurora.cluster-ro-claw3fuzkdac.us-east-1.rds.amazonaws.com"
    PORT = "5432"
    USR = "derp8_expansion_ro"
    REGION = "us-east-1"
    DBNAME = "derp8_expansion"
    Password = "P@$$word123ro"

    connection = psycopg2.connect(
        host = ENDPOINT,
        port = 5432,
        user = USR,
        password = Password,
        database=DBNAME
        )
    sql =      """SELECT *  FROM data_clean_processed WHERE timestamp in (
        select generate_series(timestamp '2021-09-01 09:00:00', 
                               timestamp '2021-10-04 16:50:00',
                               '1 minute'::interval))
							   ORDER BY timestamp;"""


    # """ SELECT * FROM public.basic_transformed_processed ORDER BY timestamp DESC FETCH FIRST ROW ONLY;"""


    xa=pd.read_sql(sql, con=connection)
    return xa


xa=getdata()
print(xa[xa['variable_name'] == 'act-hose-diameter-1']['timestamp'])

# def get_wind_data(start, end):
#     """
#     Query wind data rows between two ranges
#
#     :params start: start row id
#     :params end: end row id
#     :returns: pandas dataframe object
#     """
#
#     con = sqlite3.connect(str(DB_FILE))
#     statement = f'SELECT Speed, SpeedError, Direction FROM Wind WHERE rowid > "{start}" AND rowid <= "{end}";'
#     df = pd.read_sql_query(statement, con)
#     return df


# def get_wind_data_by_id(id):
#     """
#     Query a row from the Wind Table
#
#     :params id: a row id
#     :returns: pandas dataframe object
#     """
#
#     con = sqlite3.connect(str(DB_FILE))
#     statement = f'SELECT * FROM Wind WHERE rowid = "{id}";'
#     df = pd.read_sql_query(statement, con)
#     return df
