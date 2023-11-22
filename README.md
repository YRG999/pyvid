# Python Video Communicator

A simple Python video communications tool for 1-to-1 video chats.

1. Follow [Setup](#setup) steps below.
2. Run `python capture_video.py`.
3. Browse to `http://127.0.0.1:5001/video_feed`.
4. Accept any camera permissions.

You should see your self-view on the browser page.

> More features coming soon!

## Setup

For initial setup, create a virtual environment & run it:

```bash
$ python -m venv venv
$ . venv/bin/activate
```

Then install requirements:

```shell
$ pip install -r requirements.txt
```

*Thereafter, just run the second venv line to activate the virtual environment.*

To run samples type `python` and the file name. For example:

```shell
$ python capture_video.py
```

## Notes
* [Programming notes](doc/notes.md)
* [chatGPT discussion](doc/chat.md)
