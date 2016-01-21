/*
  Script to create a text file with mail addresses of all users in peopledb
  which have not assigned the employee.extended role.

  Call this script with "db2 -tvf selectNoExtendedRole.sql", it will generate a
  result file named mail.txt

  You can copy this script to DMGR/bin and use it like:
  wsadmin.sh -lang jython -c 'ProfilesService.setBatchRole(EMPLOYEE_EXTENDED, "mail.txt")'

  Then all users get the role EMPLOYEE_EXTENDED

  --
  
  Author: Christoph Stoettner
  E-Mail: christoph.stoettner@stoeps.de
  Date: 2016-01-20
  (c)2016 by Christoph Stoettner

  Licence: Apache License 2.0 (http://www.apache.org/licenses/LICENSE-2.0.html)
 */

connect to peopledb;
EXPORT TO mail.txt OF DEL MODIFIED by NOCHARDEL
select e.PROF_MAIL FROM EMPINST.EMPLOYEE e
    inner join EMPINST.EMP_ROLE_MAP r
    on r.PROF_KEY=e.PROF_KEY
    where r.ROLE_ID!='employee.extended';
connect reset;
