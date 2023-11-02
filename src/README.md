This is a target test repo for pushing from one to another via a Workflow.

The workflows which push to this repo can be found in
[waylan/test-repo-source](https://github.com/waylan/test-repo-source).

This repo should contain only two files. This README and a file with a
filename which consists of the date and time of the last successful build.
The date and time can be used to confirm whether the most recent attmept
sucedded. If multiple such files exist, then the workflow failed to remove
all but the newest file.
