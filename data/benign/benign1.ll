define i32 @main() {
entry:
  %0 = alloca i32
  store i32 0, i32* %0
  %1 = load i32, i32* %0
  %2 = add i32 %1, 10
  ret i32 %2
}