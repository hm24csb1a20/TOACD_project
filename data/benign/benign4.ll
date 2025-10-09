; recursive factorial: fib-like recursion but factorial
declare i32 @printf(i8*, ...)

@fmt = private constant [4 x i8] c"%d\0A\00"

define i32 @factorial(i32) {
entry:
  %n = alloca i32
  store i32 %0, i32* %n
  %nv = load i32, i32* %n
  %is1 = icmp sle i32 %nv, 1
  br i1 %is1, label %ret1, label %recur

ret1:
  ret i32 1

recur:
  %n_minus1 = sub i32 %nv, 1
  %rec = call i32 @factorial(i32 %n_minus1)
  %res = mul i32 %nv, %rec
  ret i32 %res
}

define i32 @main() {
entry:
  %res = call i32 @factorial(i32 5)
  %ptr = getelementptr [4 x i8], [4 x i8]* @fmt, i32 0, i32 0
  call i32 (i8*, ...) @printf(i8* %ptr, i32 %res)
  ret i32 0
}
