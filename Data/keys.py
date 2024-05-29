import snowflake.connector as snow

def get_openai_api_key():
    key = ''
    return key

def get_snowflake_conn():
    conn = snow.connect(
    user="",
    password="",
    account="",
    warehouse="",
    database="",
    schema="")
    return conn

def get_palm2_api_key():
    key = ''
    return key