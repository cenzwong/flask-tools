# export FLASK_APP=app.py
# export FLASK_ENV=development # will reload itself on code changes
# export FLASK_APP=./app.py; export FLASK_ENV=development
# flask run
# flask run --host=0.0.0.0
# file name should be app.py or wsgi.py
# https://flask.palletsprojects.com/en/1.1.x/patterns/lazyloading/#converting-to-centralized-url-map


from flask import Flask
from flask import request


app = Flask(__name__)
if __name__ == "__main__":
   app.run(host='0.0.0.0')

@app.route('/')
@app.route('/help')
def index():
    return "render_template(rootdoc)"

# tempdb
import app_tempdb as tempdb
app.add_url_rule(tempdb.url_prefix + "/set/<key>", view_func=tempdb.tempdb_set)
app.add_url_rule(tempdb.url_prefix + "/get/<key>", view_func=tempdb.tempdb_get)
app.add_url_rule(tempdb.url_prefix + "/clear/<key>", view_func=tempdb.tempdb_clear)
app.add_url_rule(tempdb.url_prefix + "/getAll", view_func=tempdb.tempdb_getAll)
app.add_url_rule(tempdb.url_prefix + "/clearAll", view_func=tempdb.tempdb_clearAll)

# base64
import app_base64 as ab64
app.add_url_rule(ab64.url_prefix + "/<encode_decode>", view_func=ab64.enconde_decode)
