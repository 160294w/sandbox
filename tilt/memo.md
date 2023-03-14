- install
```
curl -fsSL https://raw.githubusercontent.com/tilt-dev/tilt/master/scripts/install.sh | bash

+ brew bundle --file=-
Running `brew update --auto-update`...
==> Auto-updated Homebrew!
Updated 3 taps (homebrew/bundle, homebrew/core, and homebrew/cask).

You have 32 outdated formulae and 2 outdated casks installed.
You can upgrade them with brew upgrade
or list them with brew outdated.

Installing tilt
Homebrew Bundle complete! 1 Brewfile dependency now installed.
+ set +x
Tilt installed!
For the latest Tilt news, subscribe: https://tilt.dev/subscribe
Run `tilt up` to start.
```


- tilt up
```
❯ tilt up

───────────────────────────────────────────────────────────
 🎉  Tiltfile generated at Tiltfile
───────────────────────────────────────────────────────────

Tilt started on http://localhost:10350/
v0.31.2, built 2023-02-10

(space) to open the browser
(s) to stream logs (--stream=true)
(t) to open legacy terminal mode (--legacy=true)
(ctrl-c) to exit
Opening browser: http://localhost:10350/
```