csv_file = '//path//to//local//sales8.csv'

sqls = [[
        "PUT file://" + csv_file + " @CSV_SNOWPIPE auto_compress=true","alter pipe demo_snowpipe_poc_pipe refresh"
    ]]