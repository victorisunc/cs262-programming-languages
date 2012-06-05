var a = 1;
var x = 2;
var y = 2;
function myfun(x) {
        var a = 3;
        x = x + y;
        y = x + y;
        var p = function(y,z) {
                var q = function(x,z) {
                        return x+a*y/z;
                } ;
                return q;
        } ;
        while (x < y && (x < 10)) {
                if (! (x < y)) {
                        x = x - 1;
                } else {
                        x = x + 1;
                }
                a = a + 1;
        }
        return p(a,y);
}
var f = myfun(y);
write( f(6,7) ) ;