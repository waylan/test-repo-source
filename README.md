This is a source test repo for pushing from one to another via a Workflow.

The content of this repo is not partiucularly interesting. However, you may
find various workflows which use different methods and/or actions for pushing
from one repo to another.

This repo contains a build script which generates a file with the date and
time as the filename. That way it is easy to confirm at a glance that the
target repo received the update. It also will demonstrate whether the
preexisting file with the old date and time was removed/replaced or not. A
static file is also included which consists of the README for the target
repo.

The source files which the build script copies from are found in `src` and the
generated files are written to `output`. Any workflows should run the build
script and then copy the contents of `output` and push them to the root of
the target repo. The `ouput` directory is not commited to the repo but only
exists in the working tree.
