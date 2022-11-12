from application import app
import os
if os.path.exists("env.py"):
    import env
'''
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
'''

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)