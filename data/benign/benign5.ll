define i32 @fact_tail(i32, i32)

define i32 @fact_tail(i32 %n, i32 %acc) {
entry:
  %is_zero = icmp sle i32 %n, 1
  br i1 %is_zero, label %done, label %cont

cont:
  %n1 = sub i32 %n, 1
  %acc2 = mul i32 %acc, %n
  br label %recurse

recurse:
  ret i32 call i32 @fact_tail(i32 %n1, i32 %acc2)

done:
  ret i32 %acc
}

define i32 @main() {
entry:
  %r = call i32 @fact_tail(i32 5, i32 1)
  ret i32 %r
}
