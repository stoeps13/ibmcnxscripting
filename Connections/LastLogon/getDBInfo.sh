# Communities
	db2 "connect to sncomm" 
	db2 "select LASTLOGIN,EMAIL,DISPLAY from SNCOMM.MEMBERPROFILE WHERE LASTLOGIN IS NOT NULL ORDER BY LASTLOGIN" > communities.txt
	db2 "connect reset"
# HOMEPAGE
	db2 "connect to homepage"
	db2 "SELECT LAST_UPDATE,USER_MAIL,DISPLAYNAME from HOMEPAGE.PERSON WHERE LAST_UPDATE IS NOT NULL ORDER BY LAST_UPDATE" > homepage.txt
	db2 "connect reset"
# Activies
	db2 "connect to opnact"
	db2 "SELECT LASTLOGIN,EMAIL,MEMBERDISP from ACTIVITIES.OA_MEMBERPROFILE WHERE LASTLOGIN IS NOT NULL ORDER BY LASTLOGIN" > opnact.txt
	db2 "connect reset"
# Blogs
	db2 "connect to blogs"
	db2 "SELECT LASTLOGIN,EMAILADDRESS,FULLNAME from BLOGS.ROLLERUSER WHERE LASTLOGIN IS NOT NULL ORDER BY LASTLOGIN" > blogs.txt
	db2 "connect reset"
# Wikis
	db2 "connect to wikis"
	db2 "SELECT LAST_VISIT,EMAIL,NAME from WIKIS.USER WHERE LAST_VISIT IS NOT NULL ORDER BY LAST_VISIT" > wikis.txt
	db2 "connect reset"
# Files
	db2 "connect to files"
	db2 "SELECT LAST_VISIT,EMAIL,NAME from FILES.USER WHERE LAST_VISIT IS NOT NULL ORDER BY LAST_VISIT" > files.txt
	db2 "connect reset"
# Bookmarks
	db2 "connect to dogear"
	db2 "SELECT LASTLOGIN,EMAIL,DISPLAYNAME from DOGEAR.PERSON WHERE LASTLOGIN IS NOT NULL ORDER BY LASTLOGIN" > dogear.txt
	db2 "connect reset"
# Forums
	db2 "connect to forums"
	db2 "SELECT LASTLOGIN,EMAIL,MEMBERDISP from FORUM.DF_MEMBERPROFILE WHERE LASTLOGIN IS NOT NULL ORDER BY LASTLOGIN" > forums.txt
	db2 "connect reset"
