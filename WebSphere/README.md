The Connections adminstration scripts have moved! Please use
http://github.com/stoeps13/ibmcnx2

This repository is only used to collect some additional stuff.

# `clusterTrace.py`

To activate a trace setting on all cluster members, you can use this script.

## Activate some trace strings

This will activate the provided trace-string on all Cluster members of the Cluster `ClusterName`

```bash
./wsadmin.sh -lang jython -f clusterTrace.py ClusterName "trace-string"
```

## Disable trace

If you just use the ClusterName as an option, all traces on the Cluster members will be deactivated.

```bash
./wsadmin.sh -lang jython -f clusterTrace.py ClusterName
```
