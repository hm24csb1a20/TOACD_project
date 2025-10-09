define i32 @malware() {
entry:
  ; compute fib(6) iteratively
  %a = alloca i32
  %b = alloca i32
  store i32 0, i32* %a
  store i32 1, i32* %b
  %i = alloca i32
  store i32 0, i32* %i

  br label %loop

loop:
  %i_val = load i32, i32* %i
  %cmp = icmp slt i32 %i_val, 6
  br i1 %cmp, label %body, label %done

body:
  %aval = load i32, i32* %a
  %bval = load i32, i32* %b
  %next = add i32 %aval, %bval
  store i32 %bval, i32* %a
  store i32 %next, i32* %b
  %i_next = add i32 %i_val, 1
  store i32 %i_next, i32* %i
  br label %loop

done:
  %res = load i32, i32* %b
  ret i32 %res
}
