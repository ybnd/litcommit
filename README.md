# Library management

The library is periodically backed up by committing to the `git` repository. This is done by the `litcommit` service, which calls `commit_changes.py` around the hours listed in the `config` file.

## Setup

1. Open `cmd` as administrator

2. `cd` to `\Literature\_mgmt`

3. Install `litcommit` as a Windows service and start it up.

   ​	``` python litcommit.py install```

   ​	`NET START litcommit`

   * For some reason, it is possible that Python is not in `%PATH%` when `cmd` is opened with administrator privileges; in that case add `python.exe` to `%PATH%` or run

     `C:/Users/<USER>/Local/Programs/Python/Python37-32/python litcommit.py install`

4. To automatically start the service on boot, open 'Services' as administrator, find `litcommit`, open its Properties and set it to 'Automatic'.



## Troubleshooting

Sometimes, everything has been broken for like 2 months and you don't notice and then it appears that you can't fix it right away and I won't even be using this PC in 5 months from now and urgh Windows is annoying so why even bother.

## Configuration

The service is configured with `config.yaml`. 