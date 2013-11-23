# ConfigureConnectionsRolesRestricted
# 
# Author: Klaus Bild
# E-Mail: 

# Variables for Usermapping
connwasadmin = 'wasadmin'
connadmin = 'Admin1|Admin2'
connmoderators = 'Moderator1|Moderator2'
connmetrics = 'Metrics1|Metrics2'
connmobile = 'Mobile1|Mobile2'

# Variables for Groupmapping
connadmingroup = 'CNXAdmins'
connmoderatorgroup = 'CNXModerators'
connmetricsgroup = 'CNXMetricsAdmins'
connmobilegroup = 'CNXMobileAdmins'


appName = 'Activities'
AdminApp.edit( appName, '[-MapRolesToUsers [["person" No Yes "" ""] ["everyone" Yes No "" ""] ["reader" Yes No "" ""] ["metrics-reader" No Yes "" ""] ["search-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["widget-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["bss-provisioning-admin" No No "" ""] ]]' )
print "Setting Roles and Users for Activities"
AdminConfig.save()

appName = 'Blogs'
AdminApp.edit( appName, '[-MapRolesToUsers [["person" No Yes "" ""] ["everyone" Yes No "" ""] ["metrics-reader" No Yes "" ""] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["global-moderator" No No "' + connwasadmin + '|' + connmoderators + '" "' + connmoderatorgroup + '"] ["search-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["widget-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["reader" No Yes "" ""] ["bss-provisioning-admin" No No "" ""]  ]]' )
print "Setting Roles and Users for Blogs"
AdminConfig.save()

appName = 'Common'
AdminApp.edit( appName, '[-MapRolesToUsers [["person" No Yes "" ""] ["allAuthenticated" No Yes "" ""] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["everyone" Yes No "" ""] ["metrics-report-run" No No "' + connmetrics + '" "' + connmetricsgroup + '"] ["global-moderator" No No "' + connmoderators + '" "' + connmoderatorgroup + '"] ["mail-user" No Yes "" ""] ["reader" Yes No "" ""]  ]]' )
print "Setting Roles and Users for Common"
AdminConfig.save()

appName = 'Communities'
AdminApp.edit( appName, '[-MapRolesToUsers [["everyone" Yes No "" ""] ["reader" No Yes "" ""] ["person" No Yes "" ""] ["metrics-reader" No Yes "" ""] ["community-creator" No Yes "" ""] ["community-metrics-run" No Yes "" ""] ["search-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["global-moderator" No No "' + connwasadmin + '|' + connmoderators + '" "' + connmoderatorgroup + '"] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["dsx-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["widget-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["bss-provisioning-admin" No No "" ""]  ]]' )
print "Setting Roles and Users for Communities"
AdminConfig.save()

appName = 'Dogear'
AdminApp.edit( appName, '[-MapRolesToUsers [["person" No Yes "" ""] ["everyone" Yes No "" ""] ["reader" No Yes "" ""] ["metrics-reader" No Yes "" ""] ["search-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"]  ]]' )
print "Setting Roles and Users for Dogear"
AdminConfig.save()

appName = 'FNCS'
AdminApp.edit( appName, '[-MapRolesToUsers [["Authenticated" No Yes "" ""] ["Anonymous" Yes No "" ""] ]]' )
print "Setting Roles and Users for FileNet Content Store"
AdminConfig.save()

appName = 'Files'
AdminApp.edit( appName, '[-MapRolesToUsers [["everyone" Yes No "" ""] ["person" No Yes "" ""] ["reader" No Yes "" ""] ["metrics-reader" No Yes "" ""] ["everyone-authenticated" No Yes "" ""] ["files-owner" No Yes "" ""] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["search-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["widget-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["app-connector" No No "" ""] ["global-moderator" No No "' + connwasadmin + '|' + connmoderators + '" "' + connmoderatorgroup + '"] ["org-admin" No No "' + connadmin + '" "' + connadmingroup + '"] ["bss-provisioning-admin" No No "" ""]  ]]' )
print "Setting Roles and Users for Files"
AdminConfig.save()

appName = 'Forums'
AdminApp.edit( appName, '[-MapRolesToUsers [["person" No Yes "" ""] ["metrics-reader" No Yes "" ""] ["reader" No Yes "" ""] ["everyone" Yes No "" ""] ["discussThis-user" Yes No "" ""] ["search-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["widget-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["global-moderator" No No "' + connwasadmin + '|' + connmoderators + '" "' + connmoderatorgroup + '"] ["bss-provisioning-admin" No No "" ""] ["search-public-admin" No No "" ""]  ]]' )
print "Setting Roles and Users for Forums"
AdminConfig.save()

appName = 'Homepage'
AdminApp.edit( appName, '[-MapRolesToUsers [["person" No Yes "" ""] ["everyone" Yes No "" ""] ["reader" Yes No "" ""] ["metrics-reader" No Yes "" ""] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"]  ]]' )
print "Setting Roles and Users for Homepage"
AdminConfig.save()

appName = 'Metrics'
AdminApp.edit( appName, '[-MapRolesToUsers [["everyone" Yes No "" ""] ["person" No Yes "" ""] ["reader" Yes No "" ""] ["everyone-authenticated" No Yes "" ""] ["community-metrics-run" No Yes "" ""] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["metrics-report-run" No No "' + connmetrics + '" "' + connmetricsgroup + '"]  ]]' )
print "Setting Roles and Users for Metrics"
AdminConfig.save()

appName = 'Mobile'
AdminApp.edit( appName, '[-MapRolesToUsers [["everyone" Yes No "" ""] ["reader" Yes No "" ""] ["person" No Yes "" ""]  ]]' )
print "Setting Roles and Users for Mobile"
AdminConfig.save()

appName = 'Mobile Administration'
AdminApp.edit( appName, '[-MapRolesToUsers [["administrator" No No "' + connmobile + '" "' + connmobilegroup + '"] ["everyone" No Yes "" ""]  ]]' )
print "Setting Roles and Users for Mobile Administration"
AdminConfig.save()

appName = 'Moderation'
AdminApp.edit( appName, '[-MapRolesToUsers [["reader" No Yes "" ""] ["everyone-authenticated" No Yes "" ""] ["person" No Yes "" ""] ["global-moderator" No No "' + connmoderators + '" "' + connmoderatorgroup + '"]  ]]' )
print "Setting Roles and Users for Moderation"
AdminConfig.save()

appName = 'News'
AdminApp.edit( appName, '[-MapRolesToUsers [["person" No Yes "" ""] ["everyone" Yes No "" ""] ["reader" No Yes "" ""] ["sharebox-reader" Yes No "" ""] ["metrics-reader" No Yes "" ""] ["allAuthenticated" Yes No "" ""] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["search-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["widget-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["bss-provisioning-admin" No No "" ""]  ]]' )
print "Setting Roles and Users for News"
AdminConfig.save()

appName = 'Profiles'
AdminApp.edit( appName, '[-MapRolesToUsers [["everyone" Yes No "" ""] ["reader" No Yes "" ""] ["person" No Yes "" ""] ["allAuthenticated" No Yes "" ""] ["metrics-reader" No Yes "" ""] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["search-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["dsx-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["org-admin" No No ' + connadmin + ' ""] ["bss-provisioning-admin" No No "" ""]  ]]' )
print "Setting Roles and Users for Profiles"
AdminConfig.save()

appName = 'Search'
AdminApp.edit( appName, '[-MapRolesToUsers [["person" No Yes "" ""] ["everyone" Yes No "" ""] ["reader" No Yes "" ""] ["metrics-reader" No Yes "" ""] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["search-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["everyone-authenticated" No Yes "" ""]  ]]' )
print "Setting Roles and Users for Search"
AdminConfig.save()

appName = 'WebSphereOauth20SP'
AdminApp.edit( appName, '[-MapRolesToUsers [["authenticated" No Yes "" ""] ["client manager" No No "" ""]  ]]' )
print "Setting Roles and Users for WebSphereOauth20SP"
AdminConfig.save()

appName = 'WidgetContainer'
AdminApp.edit( appName, '[-MapRolesToUsers [["person" No Yes "" ""] ["allAuthenticated" No Yes "" ""] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["everyone" Yes No "" ""] ["reader" Yes No "" ""] ["metrics-reader" No No "" ""] ["global-moderator" No No "' + connmoderators + '" "' + connmoderatorgroup + '"] ["mail-user" No Yes "" ""] ["trustedExternalApplication" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"]  ]]' )
print "Setting Roles and Users for WidgetContainer"
AdminConfig.save()

appName = 'Wikis'
AdminApp.edit( appName, '[-MapRolesToUsers [["everyone" Yes No "" ""] ["person" No Yes "" ""] ["reader" No Yes "" ""] ["metrics-reader" No Yes "" ""] ["everyone-authenticated" No Yes "" ""] ["wiki-creator" No Yes "" ""] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["search-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["widget-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["bss-provisioning-admin" No No "" ""]  ]]' )
print "Setting Roles and Users for Wikis"
AdminConfig.save()

appName = 'connectionsProxy'
AdminApp.edit( appName, '[-MapRolesToUsers [["person" No Yes "" ""] ["allAuthenticated" No Yes "" ""] ["reader" Yes No "" ""] ["everyone" Yes No "" ""]  ]]' )
print "Setting Roles and Users for connectionsProxy"
AdminConfig.save()
