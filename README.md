***Disclaimer:***

***There are better ways to do this, this is just the first thing I came up with, and it works fine for now.***





# Library management

The library is periodically backed up by committing to the `git` repository. This is done by the `litcommit` service, which calls `commit_changes.py` around the hours listed in the `config` file.

## Windows background service setup

1. Open `cmd` as administrator

2. `cd` to `\Literature\_mgmt`

3. Install `litcommit` as a Windows service and start it up.

   ​	``` python litcommit.py install```

   ​	`NET START litcommit`

4. To automatically start the service on boot, open 'Services' as administrator, find `litcommit`, open its Properties and set it to 'Automatic'.

## Configuration

The service is configured with `config.yaml`. 