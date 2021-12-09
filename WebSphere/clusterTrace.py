'''
Enable / disable trace settings for all cluster members
Cluster name is passed as first parameter to the script
Tracestring is passed as second parameter

if Tracestring is empty -> disable trace

author:   Christoph Stoettner
mail:     christoph.stoettner@stoeps.de
license:  Apache 2.0
'''
import sys

if len(sys.argv) == 0:
    print('''
        \tScript needs at least one parameter: Clustername
        \n\tWhen a second parameter is used, it is interpreted as trace string
        \n\n\tExample:
        \twsadmin.sh -lang jython -f clusterTrace.py InfraCluster "*=info:com.ibm.lconn.news.*=all:com.ibm.lconn.core.services.*=all:com.ibm.lconn.hpnews.*=all"
''')
    sys.exit()
elif len(sys.argv) == 1:
    type = 'disabled'
    cluster_name=sys.argv[0]
else:
    cluster_name=sys.argv[0]
    traces=sys.argv[1]
    type = 'enabled'

if type == 'enabled':
    trace_string=''
    for trace in traces.split(':'):
       if trace_string=='':
           trace_string=trace + '=' + type
       else:
           trace_string=trace_string + ':' + trace + '=' + type
else:
    trace_string='*=info=enabled'

cluster_id = AdminConfig.getid("/ServerCluster:"+cluster_name+"/")
if not cluster_id:
    raise "Cluster %s does not exist!" % cluster_name

member_ids = AdminConfig.showAttribute(cluster_id, "members")

member_ids = member_ids[1:-1]

for member_id in member_ids.split():
    member_name=AdminConfig.showAttribute(member_id, "memberName")
    node_name=AdminConfig.showAttribute(member_id, "nodeName")

    # Get TraceServer ID
    ts=AdminControl.completeObjectName('type=TraceService,process='+member_name+',*')

    # Set trace settings
    try:
        AdminControl.setAttribute(ts, 'traceSpecification', trace_string)
        print("Successfully " + type + " trace on " + node_name + '/' + member_name)
    except:
        print("Error changing trace on " + node_name + '/' + member_name)
