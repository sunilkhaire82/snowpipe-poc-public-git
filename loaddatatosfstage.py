from snowflake_conn import *
from tablescritps import sqls



def load_csv_into_sf(cs, sqls):
    #get sequence of sql to execute
    for sqllist in sqls:
        for sql in sqllist:
            print("Executing sql", sql)
            try:
                cs.execute(sql)
            except Exception as e:
                print("uncaught exception",str(e))
        print("data load completed.....")
    cs.close()

#11976


if __name__ == "__main__":
    load_csv_into_sf(cs, sqls)
