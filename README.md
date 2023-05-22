# GHEmoji

Git hook for Gitemoji.

## Requirements

```
Python 3.8
Poetry 1.4.2
```

# Build

```
sh ./build.sh
```

# Install

```
cp ./dist/ghemoji ~/.local/bin/ghemoji
chmod +x ~/.local/bin/ghemoji
```

# Usage

Install git hook:

```
ghemoji -i "path/to/repo"
```

Uninstall git hook:

```
ghemoji -u "path/to/repo"
```
