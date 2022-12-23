import base64



code = 'CmltcG9ydCByZXF1ZXN0cwpmcm9tIHRpbWUgaW1wb3J0IHNsZWVwCmltcG9ydCByYW5kb20KCgoKCgoKCmhlYWRlcnMgPSB7CiAgICAnQWNjZXB0JzogJ2FwcGxpY2F0aW9uL2pzb24sIHRleHQvcGxhaW4sICovKicsCiAgICAnQWNjZXB0LUxhbmd1YWdlJzogJ2VuLVVTLGVuO3E9MC45JywKICAgICdDb25uZWN0aW9uJzogJ2tlZXAtYWxpdmUnLAogICAgJ09yaWdpbic6ICdodHRwczovL2Nob29zZXJlYWxsZWF0aGVyLmNvbScsCiAgICAnUmVmZXJlcic6ICdodHRwczovL2Nob29zZXJlYWxsZWF0aGVyLmNvbS8nLAogICAgJ1NlYy1GZXRjaC1EZXN0JzogJ2VtcHR5JywKICAgICdTZWMtRmV0Y2gtTW9kZSc6ICdjb3JzJywKICAgICdTZWMtRmV0Y2gtU2l0ZSc6ICdjcm9zcy1zaXRlJywKICAgICdVc2VyLUFnZW50JzogJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMDMuMC41MDYwLjEzNCBTYWZhcmkvNTM3LjM2IEVkZy8xMDMuMC4xMjY0Ljc3JywKICAgICdzZWMtY2gtdWEnOiAnIiBOb3Q7QSBCcmFuZCI7dj0iOTkiLCAiTWljcm9zb2Z0IEVkZ2UiO3Y9IjEwMyIsICJDaHJvbWl1bSI7dj0iMTAzIicsCiAgICAnc2VjLWNoLXVhLW1vYmlsZSc6ICc/MCcsCiAgICAnc2VjLWNoLXVhLXBsYXRmb3JtJzogJyJXaW5kb3dzIicsCn0KCmRhdGEgPSB7CiAgICAncHJvamVjdF9pZCc6ICc4NjAyNScsCiAgICAnY29tcGV0aXRpb25faWQnOiAnMTI1JywKICAgICdzcGVjaWFsaXNtX2lkJzogJzknLAp9CgoKd2l0aCBvcGVuKCdjb25maWcudHh0JywgJ3InKSBhcyBmOgogICAgY29uZiA9IGYucmVhZGxpbmVzKCkKICAgIHRpcGUgPSBjb25mWzBdLnN0cmlwKCkKICAgIGZpbGV0b29wZW4gPSBjb25mWzFdLnN0cmlwKCkKICAgIHRpbWVyYW5nZSA9IGNvbmZbMl0uc3RyaXAoKQogICAgdGltZTEsIHRpbWUyID0gdGltZXJhbmdlLnNwbGl0KCcsJykKCgp3aXRoIG9wZW4oZid7ZmlsZXRvb3Blbn0nLCAncicpIGFzIGY6CiAgICBuID0gZi5yZWFkbGluZXMoKQogICAgeCA9IFt6LnNwbGl0KCkgZm9yIHogaW4gbl0KCgpjb3VudCA9IDEKd2hpbGUgY291bnQgPCBsZW4oeCk6CiAgICBwb3h5ID0geFtjb3VudF0KICAgIHBveHkgPSBwb3h5WzBdCgogICAgcHJpbnQocG94eSkKICAgIGlmIHRpcGUgPT0gJ3NvY2tzNSc6CiAgICAgICAgcHJveGllcyA9IHsKICAgICAgICAgICAgImh0dHAiOmYic29ja3M1Oi8ve3BveHl9IiwKICAgICAgICAgICAgImh0dHBzIjpmInNvY2tzNTovL3twb3h5fSIKICAgICAgICB9CiAgICBlbGlmIHRpcGUgPT0gJ3NvY2tzNCc6CiAgICAgICAgcHJveGllcyA9IHsKICAgICAgICAgICAgImh0dHAiOmYic29ja3M0Oi8ve3BveHl9IiwKICAgICAgICAgICAgImh0dHBzIjpmInNvY2tzNDovL3twb3h5fSIKICAgICAgICB9CiAgICBlbGlmIHRpcGUgPT0gJ2h0dHBzJyBvciB0aXBlID09ICdodHRwJzoKICAgICAgICBwcm94aWVzID0gewogICAgICAgICAgICAiaHR0cCI6ZiJ7cG94eX0iLAogICAgICAgICAgICAiaHR0cHMiOmYie3BveHl9IgogICAgICAgIH0KICAgIGVsc2U6CiAgICAgICAgcHJpbnQoJ1BsZWFzZSBzcGVjaWZ5IHRoZSB0eXBlIG9mIHByb3hpZXMnKQoKICAgIHRyeToKICAgICAgICByZXNwb25zZSA9IHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vYXJ0c3RocmVhZC5jb20vd3AtanNvbi9hcnRzdGhyZWFkL3YxL2FwcC12b3RlJywgaGVhZGVycz1oZWFkZXJzLCBkYXRhPWRhdGEsIHByb3hpZXMgPSBwcm94aWVzKQogICAgICAgIHByaW50KCdWT1RFIEFEREVEJykKICAgICAgICBzbGVlcChyYW5kb20ucmFuZGludChpbnQodGltZTEpKiA2MCwgaW50KHRpbWUyKSAqIDYwKSkKICAgIAogICAgZXhjZXB0OgogICAgICAgIHByaW50KCJQUk9YWSBGQUlMRUQiKQoKICAgIGNvdW50ID0gY291bnQgKyAxCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCg=='
exec(base64.b64decode(code))