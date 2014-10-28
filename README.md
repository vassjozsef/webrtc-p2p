Peer-to-Peer WebRTC Sample using AppEnngine Channels
===

This is a WebRTC sample to narrow down [https://code.google.com/p/webrtc/issues/detail?id=3940](https://code.google.com/p/webrtc/issues/detail?id=3940).

Signaling is implemented using [AppEngine Channel](https://cloud.google.com/appengine/docs/python/channel/).

Usage
---

You can run locally using

    dev_appserver.py .

The application is available at [http://localhost:8080](http://localhost:8080).

To deploy, please run

    appcfg.py update . --oauth2
