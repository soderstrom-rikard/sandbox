## Presets

In order to see the complete list of presets, use

```sh
cmake --list-presets
```

The default presets are as follows

| Preset                | Details                                                                   |
|-----------------------|---------------------------------------------------------------------------|
| default               | Builds all libraries and tools natively                                   |
| default-sanitized     | Builds all libraries and tools natively and with sanitizer enabled        |

### Build with a preset

In the example below `buildX` is directory that may or may not exist
that will contain the build output and configuration of a build configured
with variable `X=true`.

```
cmake --preset default
cmake --build build/default-release
```

## Running in a browser

Type the following in a terminal to start a local web server

```
python3 -m http.server
firefox http://0.0.0.0:8000/build/emscripten-release/tools/filecast_cli.html
```

Finally open localhost:8000 in your browser to access the tools.

## Applying clang-format

```sh
git ls-files *.cpp *.h | xargs clang-format -i
```
