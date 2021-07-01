# Flask Simple Chat App

> Simple real-time chat app using Flask and plain Javascript

Real-time chat app using Flask, and plain Javascript, HTML without \
WebSockets/Socket.IO; Just simple HTTP requests back and forth \
between the Javascript frontend and Flask.

## Usage
Run the following commands to run the project on your localhost:

```bash
$ # Clone the repo to your local machine
$ git clone https://github.com/FaresAhmedb/flask-simple-chat-app.git
$ # Create a new venv
$ python3 -m venv env
$ # Install the dependencies
$ pip install -r requirements.txt
$ # Run Flask!
$ flask run
```

The last command output should be something like this:

```
 * Serving Flask app 'app/app.py' (lazy loading)
 * Environment: devolpment
 * Debug mode: on
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://XXX.XXX.X.X:XXXX/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 123-456-789
```

Replace `http://XXX.XXX.X.X:XXXX/` with your output link and \
open it in your browser.

## License

MIT License

Copyright (c) 2021 Fares Ahmed

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
