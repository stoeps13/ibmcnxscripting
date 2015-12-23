/* Copy these functions to the end of you profiles_functions.js in tdisol folder
 * Author: Christoph Stoettner
 * E-Mail: christoph.stoettner@stoeps.de
 * Blog: http://www.stoeps.de
 * Licence: Apache 2.0
 */

/* calculate FullName with SN and Givenname
 *
 * Often the fullname in AD is not filled good enough to use it in Connections,
 * then it is better to catch givenname and sn to merge these values as
 * fullname.
 *
 * */
 function func_compute_CN(fieldname) {
    var givenName = work.getAttribute("givenName");
    var sn = work.getAttribute("sn");

    if(sn != null) {
        var result = givenName + ' ' + sn;
    }
    return result;
}

/* Set an initial timezone
 * in single nation environments it is easier to set
 * the timezone here than in LDAP
 * */
function function_settimezone(fieldname){
    var timeZone = 'Europe/Amsterdam';
    result = timeZone;
    return result;
}

/* Set db field to null
 *
 * When you want to delete content in your profiles database
 * add {function_setnull} to the field in map_dbrepos_from_source
 *
 * */
function function_setnull(fieldname){
    var result = '';
    return result;
}
