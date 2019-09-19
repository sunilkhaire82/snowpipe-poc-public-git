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

git init
git add --all
git commit -m "first commit"
git remote add origin https://github.com/sunilkhaire82/snowpipe-poc-public-git.git
git push -u origin master