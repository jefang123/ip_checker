from datetime import date
import json
from flask import Flask, jsonify, request
import checkip
from fetcher import IPStorage

app = Flask(__name__)
current_ips = IPStorage()

@app.route('/checkips', methods=["POST"])
def check_ips():
  if current_ips.fetchDate != date.today():
    current_ips.refresh()
  d = request.json
  ips_value = d.get('ips', None)

  if isinstance(ips_value, list):
    ips_value = [i for i in ips_value if checkip.check(i)]
  else:
    return jsonify({'status': 400, 'reason': 'invalid json provided, check ips key and value'})
  
  if len(ips_value):
    matches = [i for i in ips_value if i in current_ips.ips]
    return str(len(matches)) + "\n"
  else:
    return jsonify({'status': 400, 'reason': 'invalid ips given'})
  
if __name__ == '__main__':
  app.run(port=5000)