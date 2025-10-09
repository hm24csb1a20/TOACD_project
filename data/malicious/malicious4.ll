; Declare external puts
declare i32 @puts(i8*)

@.str = private constant [14 x i8] c"Hello, world!\00"

define i32 @malware() {
entry:
  %0 = getelementptr [14 x i8], [14 x i8]* @.str, i32 0, i32 0
  %1 = call i32 @puts(i8* %0)
  ret i32 0
}
