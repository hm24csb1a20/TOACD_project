define i32 @malware() {
entry:
  ; N = 10
  %N = alloca i32
  store i32 10, i32* %N

  %i = alloca i32
  store i32 1, i32* %i

  %sum = alloca i32
  store i32 0, i32* %sum

  br label %loop

loop:
  %i_val = load i32, i32* %i
  %cmp = icmp sle i32 %i_val, 10
  br i1 %cmp, label %body, label %done

body:
  %cur = load i32, i32* %sum
  %new = add i32 %cur, %i_val
  store i32 %new, i32* %sum
  %i_next = add i32 %i_val, 1
  store i32 %i_next, i32* %i
  br label %loop

done:
  %result = load i32, i32* %sum
  ret i32 %result
}
