import json,os,urllib.request,urllib.parse
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
from pathlib import Path
KEY=os.getenv("TWELVE_DATA_API_KEY","")
class Handler(BaseHTTPRequestHandler):
 def do_GET(self):
  path=self.path.split("?")[0]
  if path=="/api/health":
   return self.send_json({"status":"ok","provider":"Twelve Data","configured":bool(KEY)})
  if path=="/api/candles":
   if not KEY:return self.send_json({"error":"TWELVE_DATA_API_KEY not configured"},503)
   params=urllib.parse.urlencode({"symbol":"XAU/USD","interval":"15min","outputsize":100,"apikey":KEY})
   try:
    with urllib.request.urlopen("https://api.twelvedata.com/time_series?"+params,timeout=15) as resp:data=json.load(resp)
    if data.get("status")=="error" or "values" not in data:return self.send_json({"error":data.get("message","Provider returned no candles")},502)
    return self.send_json({"symbol":"XAU/USD","interval":"15min","values":data["values"],"provider":"Twelve Data"})
   except Exception:return self.send_json({"error":"Provider unavailable"},502)
  if path in ("/","/index.html"):
   content=Path(__file__).with_name("index.html").read_bytes()
   self.send_response(200);self.send_header("Content-Type","text/html; charset=utf-8");self.send_header("Content-Length",str(len(content)));self.end_headers();self.wfile.write(content);return
  self.send_error(404)
 def send_json(self,data,status=200):
  raw=json.dumps(data).encode();self.send_response(status);self.send_header("Content-Type","application/json");self.send_header("Cache-Control","no-store");self.send_header("Content-Length",str(len(raw)));self.end_headers();self.wfile.write(raw)
if __name__=="__main__":ThreadingHTTPServer(("0.0.0.0",int(os.getenv("PORT","8000"))),Handler).serve_forever()
