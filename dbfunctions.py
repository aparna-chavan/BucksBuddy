from imports import *
import keys

# Function to save chat context to Snowflake
def save_chat_context(ticker, context):
    conn = keys.get_snowflake_conn()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO chat_contexts(ticker, reddit_context, twitter_context, fin_context, pred_context) VALUES(%s, %s, %s, %s)", (ticker, context["reddit_context"], context["twitter_context"], context["fin_context"], context["pred_context"]))
        conn.commit()
    finally:
        cursor.close()
        conn.close()


def get_chat_context(ticker):
    conn = keys.get_snowflake_conn()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT context FROM chat_contexts WHERE user_id = %s", (ticker,))
        result = cursor.fetchone()
        return result[0] if result else None
    finally:
        cursor.close()
        conn.close()

def get_context():
    conn = keys.get_snowflake_conn()
    cur = conn.cursor()
    sql = 'select * from "context_data"'
    cur.execute(sql)
    context = cur.fetch_pandas_all()
    return context
