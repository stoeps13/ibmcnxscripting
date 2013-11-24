/* Copy these functions to the end of you profiles_functions.js in tdisol folder
 * Author: Christoph Stoettner
 * E-Mail: christoph.stoettner@stoeps.de
 * Blog: http://www.stoeps.de
 * Licence: Apache 2.0
 */

/* calculate FullName with SN and Givenname */
 function func_compute_CN(fieldname) {
    var givenName = work.getAttribute("givenName");
    var sn = work.getAttribute("sn");
 
    if(sn != null) {
        var result = givenName + ' ' + sn;
    }
    return result;
}

/* Set an initial timezone */
function function_settimezone(fieldname){
    var timeZone = 'Europe/Amsterdam';
    result = timeZone;
    return result;
}

/* Set db field to null */
function function_setnull(fieldname){
    var result = '';
    return result;
}