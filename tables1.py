from flask_table import Table, Col

class Throws(Table):
    id = Col('id')
    name = Col('name')
    meetdate = Col('meetdate')
    spresult = Col('spresult')