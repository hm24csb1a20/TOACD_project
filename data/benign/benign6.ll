declare i32 @puts(i8*)

@hello = private constant [13 x i8] c"hello world\0A\00"

define i32 @strlen(i8*) {
entry:
  %p = alloca i8*
  store i8* %0, i8** %p
  %idx = alloca i32
  store i32 0, i32* %idx
  br label %loop

loop:
  %i = load i32, i32* %idx
  %ptr = load i8*, i8** %p
  %cur = getelementptr i8, i8* %ptr, i32 %i
  %ch = load i8, i8* %cur
  %iszero = icmp eq i8 %ch, 0
  br i1 %iszero, label %done, label %inc

inc:
  %i2 = add i32 %i, 1
  store i32 %i2, i32* %idx
  br label %loop

done:
  %res = load i32, i32* %idx
  ret i32 %res
}

define i32 @main() {
entry:
  %ptr = getelementptr [13 x i8], [13 x i8]* @hello, i32 0, i32 0
  %len = call i32 @strlen(i8* %ptr)
  ; print length using puts by formatting not included to keep simple
  ret i32 %len
}
