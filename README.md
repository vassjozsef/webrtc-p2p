Peer-to-Peer WebRTC Sample using AppEnngine Channels
===

This is a WebRTC sample to narrow down [https://code.google.com/p/webrtc/issues/detail?id=3940](https://code.google.com/p/webrtc/issues/detail?id=3940).

Signaling is implemented using [AppEngine Channel](https://cloud.google.com/appengine/docs/python/channel/).

The application is hosted at [https://webrtc-p2p.appspot.com](https://webrtc-p2p.appspot.com).

Audio Issue Reproduction
---
We use two MacBook Air laptops in the same network to reproduce the issue. Make sure that the caller has USB headset and Sound Preferences are set for USB headset for both Input and Output. Please perform the followings:

1. Load caller https://webrtc-p2p.appspot.com/?user=a. Click Connect and make sure you are connected.
1. Load caller https://webrtc-p2p.appspot.com/?user=b. Click Connect and make sure you are connected.
1. From caller, call `b`, allow microphone access if prompted.
1. On the callee, allow microphone access if prompted. The call will connect automatically.
1. Make sure that ICE is complete, you should see `ICE state: completed`
1. Make sure both party hear audio
1. On caller, click Hangup

Repeat Steps 3-7 a few times. You should see ICE completed but callee does not hear audio. Caller receives audio.


Known Issues
--
1. ICE may not connect every time. Simply hangup and try again.
2. Firefox is not supported.
3. No ICE servers are specifed. Make sure that the two computers are on the same network.


Deployment
---

You can run locally using

    dev_appserver.py .

The application is available at [http://localhost:8080](http://localhost:8080).

To deploy, please run

    appcfg.py update . --oauth2
