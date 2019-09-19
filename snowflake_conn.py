import snowflake.connector

import datetime

ctx = snowflake.connector.connect(user='user',
                                  password='password',
                                  account='<snowflake account>')
cs = ctx.cursor()

# deinfe a role to be used

cs.execute("USE ROLE <role>")

# define a warehoues to be used

cs.execute("USE WAREHOUSE <warehouse>")

# define a schema to be used

cs.execute('USE SCHEMA DEMO_DB.PUBLIC')

